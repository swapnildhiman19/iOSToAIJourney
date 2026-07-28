"""Async boundary lab: fan-out shape and the blocking boundary, measured.

Run:
    cd "AI Solutions Platform"
    uv run --locked --extra dev python \
        diagnostics/Sprint-01-AI-Software-Foundations/async_boundary_lab.py
"""

from __future__ import annotations

import asyncio
import contextlib
import time
from collections.abc import Iterator

CALL_COUNT = 50
DEPENDENCY_LATENCY_SECONDS = 0.10
CONCURRENCY_LIMIT = 5
BLOCKING_DURATION_SECONDS = 1.0
QUICK_LATENCY_SECONDS = 0.05
QUICK_CALL_COUNT = 4

class InFlightMeter:
    """Track simultaneous dependency calls and remember the peak."""

    def __init__(self) -> None:
        self._current = 0
        self.peak = 0

    @contextlib.contextmanager
    def track(self) -> Iterator[None]:
        self._current += 1
        self.peak = max(self.peak, self._current)
        try:
            yield
        finally:
            # finally, not a trailing statement: an exception or a cancellation
            # inside the call must still decrement, or peak becomes a lie.
            self._current -= 1

class FakeSlowDependency:
    """A stand-in for a slow remote dependency with fixed latency."""

    def __init__(self, latency_seconds: float, meter: InFlightMeter) -> None:
        self._latency_seconds = latency_seconds
        self._meter = meter

    async def call(self, index: int) -> int:
        with self._meter.track():
            await asyncio.sleep(self._latency_seconds)
        return index

async def scenario_unbounded_fan_out() -> tuple[float, int]:
    """launch CALL_COUNT calls with no limit.

    Return (wall_clock_seconds, peak_in_flight).
    Time it with time.perf_counter() around the await, not around task creation.
    Expect: wall ~= one latency; peak == CALL_COUNT.
    """
    meter = InFlightMeter()
    dep = FakeSlowDependency(DEPENDENCY_LATENCY_SECONDS, meter)
    tasks = [asyncio.create_task(dep.call(i)) for i in range(CALL_COUNT)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    wall = time.perf_counter() - start
    return wall, meter.peak


async def scenario_bounded_fan_out() -> tuple[float, int]:
    """same fan-out, gated by asyncio.Semaphore(CONCURRENCY_LIMIT).

    Return (wall_clock_seconds, peak_in_flight).
    Use `async with semaphore:` so the permit is returned on error and cancel.
    Expect: peak == CONCURRENCY_LIMIT exactly;
            wall ~= ceil(CALL_COUNT / CONCURRENCY_LIMIT) * latency.
    """
    meter = InFlightMeter()
    dep = FakeSlowDependency(DEPENDENCY_LATENCY_SECONDS, meter)
    sem = asyncio.Semaphore(CONCURRENCY_LIMIT)

    async def worker(i: int) -> int:
        async with sem:
            return await dep.call(i)

    tasks = [asyncio.create_task(worker(i)) for i in range(CALL_COUNT)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    wall = time.perf_counter() - start
    return wall, meter.peak


async def scenario_starvation(*, offload_blocking_call: bool) -> list[float]:
    """the blocking boundary. This one is the point of the block.

    Run ONE coroutine that consumes BLOCKING_DURATION_SECONDS, and
    QUICK_CALL_COUNT coroutines that `await asyncio.sleep(QUICK_LATENCY_SECONDS)`.
    Return each quick coroutine's completion time, measured from a single
    perf_counter() taken before anything is scheduled.

    offload_blocking_call is False -> call time.sleep(BLOCKING_DURATION_SECONDS)
                                      directly inside the coroutine.
    offload_blocking_call is True  -> await asyncio.to_thread(time.sleep, ...).

    Schedule the blocking coroutine FIRST so the starvation is unambiguous.
    Expect False -> ~1.05s each;  True -> ~0.055s each.
    """
    async def do_blocking() -> None:
        if offload_blocking_call:
            await asyncio.to_thread(time.sleep, BLOCKING_DURATION_SECONDS)
        else:
            time.sleep(BLOCKING_DURATION_SECONDS)

    async def do_quick() -> float:
        await asyncio.sleep(QUICK_LATENCY_SECONDS)
        return time.perf_counter() - start_time

    start_time = time.perf_counter()
    blocking_task = asyncio.create_task(do_blocking())
    quick_tasks = [asyncio.create_task(do_quick()) for _ in range(QUICK_CALL_COUNT)]
    results = await asyncio.gather(blocking_task, *quick_tasks)
    return list(results[1:])

async def main() -> None:
    unbounded_wall, unbounded_peak = await scenario_unbounded_fan_out()
    bounded_wall, bounded_peak = await scenario_bounded_fan_out()
    starved = await scenario_starvation(offload_blocking_call=False)
    recovered = await scenario_starvation(offload_blocking_call=True)

    print("=== 1. unbounded fan-out ===")
    print(f"calls={CALL_COUNT} wall={unbounded_wall:.3f}s peak={unbounded_peak}")
    print("=== 2. semaphore-bounded fan-out ===")
    print(f"limit={CONCURRENCY_LIMIT} wall={bounded_wall:.3f}s peak={bounded_peak}")
    print("=== 3. blocking boundary ===")
    print(f"before fix (time.sleep):  {[f'{s:.3f}' for s in starved]}")
    print(f"after  fix (to_thread):   {[f'{s:.3f}' for s in recovered]}")

if __name__ == "__main__":
    asyncio.run(main())
