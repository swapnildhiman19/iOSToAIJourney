"""Sanity check that python-dotenv loads .env correctly.

Run with:
    uv run python check_env.py
"""
import os

from dotenv import load_dotenv

load_dotenv()

keys = ["GOOGLE_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_CLOUD_PROJECT"]
for k in keys:
    val = os.environ.get(k)
    status = "✅ set" if val else "⚠️  empty (fill in Day 1 lesson 4–6 or Day 4 lesson)"
    masked = (val[:6] + "…" + val[-4:]) if val and len(val) > 12 else val
    print(f"{k:30s} {status:60s} {masked or ''}")
