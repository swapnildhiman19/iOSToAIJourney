"""
Week 1 verification script.

Runs every hello-world built across Days 1-6 and prints PASS/FAIL for each.
Usage:
    python scripts/week1_verify.py

Exit code:
    0 if all checks pass, 1 otherwise.
"""

from __future__ import annotations

import os
import sys
import time
from dataclasses import dataclass
from typing import Callable

from dotenv import load_dotenv

load_dotenv()


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str
    elapsed_s: float


def _time(fn: Callable[[], tuple[bool, str]]) -> tuple[bool, str, float]:
    t0 = time.time()
    try:
        ok, detail = fn()
    except Exception as exc:  # noqa: BLE001 — we want to capture any failure
        return False, f"{type(exc).__name__}: {exc}", time.time() - t0
    return ok, detail, time.time() - t0


# ---------- 1. Gemini via AI Studio ----------
def check_gemini_aistudio() -> tuple[bool, str]:
    from google import genai

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return False, "GOOGLE_API_KEY not set in .env"
    client = genai.Client(api_key=api_key)
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say PONG in one word.",
    )
    text = (resp.text or "").strip()
    return ("pong" in text.lower(), f"replied: {text[:40]!r}")


# ---------- 2. Anthropic Claude ----------
def check_anthropic() -> tuple[bool, str]:
    import anthropic

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return False, "ANTHROPIC_API_KEY not set in .env"
    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16,
        messages=[{"role": "user", "content": "Say PONG in one word."}],
    )
    text = "".join(b.text for b in msg.content if hasattr(b, "text")).strip()
    return ("pong" in text.lower(), f"replied: {text[:40]!r}")


# ---------- 3. Gemini via Vertex ----------
def check_gemini_vertex() -> tuple[bool, str]:
    from google import genai

    project = os.environ.get("GOOGLE_CLOUD_PROJECT")
    if not project:
        return False, "GOOGLE_CLOUD_PROJECT not set"
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")
    client = genai.Client(vertexai=True, project=project, location=location)
    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say PONG in one word.",
    )
    text = (resp.text or "").strip()
    return ("pong" in text.lower(), f"replied: {text[:40]!r}")


# ---------- 4. Gemma 3 local via MLX ----------
def check_gemma_local() -> tuple[bool, str]:
    try:
        from mlx_lm import generate, load
    except ImportError:
        return False, "mlx-lm not installed in this venv"
    model, tokenizer = load("mlx-community/gemma-3-1b-it-4bit")
    response = generate(
        model,
        tokenizer,
        prompt="Say PONG in one word.",
        max_tokens=16,
        verbose=False,
    )
    text = response.strip()
    return (len(text) > 0, f"generated: {text[:40]!r}")


# ---------- 5. AWS STS identity ----------
def check_aws_sts() -> tuple[bool, str]:
    import boto3

    sts = boto3.client("sts")
    ident = sts.get_caller_identity()
    arn = ident.get("Arn", "")
    if not arn:
        return False, "no Arn in response"
    if arn.endswith(":root"):
        return False, f"using root user! Switch to IAM admin. Arn={arn}"
    return True, arn


CHECKS: list[tuple[str, Callable[[], tuple[bool, str]]]] = [
    ("Gemini (AI Studio)", check_gemini_aistudio),
    ("Anthropic Claude  ", check_anthropic),
    ("Gemini (Vertex)   ", check_gemini_vertex),
    ("Gemma 3 1B local  ", check_gemma_local),
    ("AWS STS identity  ", check_aws_sts),
]


def main() -> int:
    print("=== Week 1 Verification ===")
    results: list[CheckResult] = []
    for idx, (name, fn) in enumerate(CHECKS, start=1):
        ok, detail, elapsed = _time(fn)
        mark = "✅" if ok else "❌"
        print(f"{idx}. {name} {mark}  {elapsed:5.1f}s  {detail}")
        results.append(CheckResult(name=name, ok=ok, detail=detail, elapsed_s=elapsed))
    print()
    passed = sum(1 for r in results if r.ok)
    total = len(results)
    if passed == total:
        print(f"{passed}/{total} checks passed. Week 1 stack is healthy. 🎉")
        return 0
    print(f"{passed}/{total} checks passed. Failing:")
    for r in results:
        if not r.ok:
            print(f"  - {r.name.strip()}: {r.detail}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
