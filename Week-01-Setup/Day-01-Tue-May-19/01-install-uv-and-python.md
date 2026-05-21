# 01 — Install `uv` and Python 3.12

## 🧒 Layman explanation

`uv` is a single tiny program (written in Rust) that does *everything* you used to do with five separate Python tools (`pip`, `pip-tools`, `virtualenv`, `pyenv`, `pipx`) — but ~10–100× faster and with a single config file.

You install `uv` once. After that, every Python project on your machine starts with `uv init` (like `git init`) and uses `uv add <package>` (like `npm install <package>`). It's how modern Python projects start in 2026.

You also need **Python 3.12** because that's what FastAPI + Pydantic v2 + modern type-syntax all assume. `uv` will install it for you — you don't need to install Python yourself.

---

## 🔧 Technical deep-dive

### What `uv` actually replaces

| You used to use…        | Now you use…                   | Speed-up    |
|-------------------------|--------------------------------|-------------|
| `pyenv install 3.12`    | `uv python install 3.12`       | ~5× faster  |
| `python -m venv .venv`  | (automatic — created on demand)| ~10× faster |
| `pip install -r reqs`   | `uv sync`                      | ~10–100×    |
| `pip-compile`           | `uv lock`                      | ~50×        |
| `pipx install <tool>`   | `uv tool install <tool>`       | ~50×        |
| `requirements.txt`      | `pyproject.toml` + `uv.lock`   | Type-safer  |

### How `uv` works under the hood (briefly)

- Written in **Rust** → fast cold starts (< 10ms), parallel resolution
- Maintains a **global cache** in `~/.cache/uv/` — installing the same package twice across projects re-uses the disk copy via hardlinks
- Uses a **proper SAT solver** for dependency resolution (pip's resolver is heuristic and slow)
- Produces a **deterministic lockfile** (`uv.lock`) — your CI machine + Cloud Run + colleague's laptop all get bit-identical environments

---

## 💻 Hands-on — install `uv`

Run this **once** on your Mac. It uses the official installer:

```bash
# Install uv (the recommended way)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload your shell so 'uv' is on PATH
exec $SHELL -l

# Verify it installed
uv --version
# Expected output:  uv 0.x.y  (Homebrew on macOS)

# Install Python 3.12 (uv manages multiple Python versions for you)
uv python install 3.12

# Verify Python is available to uv
uv python list
# Expected output: includes 3.12.x and likely your system Python
```

### Common installation issues

| Symptom                                         | Fix                                                                     |
|-------------------------------------------------|-------------------------------------------------------------------------|
| `uv: command not found` after install           | Run `exec $SHELL -l` or open a new terminal tab                          |
| Behind a corporate proxy                        | Set `HTTPS_PROXY=http://proxy.walmart.com:8080` before running install   |
| `curl` says certificate error                   | Walmart's corporate cert chain — install via `brew install uv` instead    |
| Multiple Pythons on Mac confuse you             | That's fine — `uv` will pick the right one per project                   |

### Alternative install (if `curl` fails)

```bash
brew install uv
```

Brew also works and is fully supported. Astral publishes a Homebrew tap.

---

## 📊 Where `uv` files live on your disk

```
~/.cache/uv/                            ← global package cache (deduped via hardlinks)
~/.local/share/uv/python/cpython-3.12.../  ← uv-managed Python interpreters

<your-project>/
├── pyproject.toml                       ← project config + dependencies (you edit this)
├── uv.lock                              ← deterministic lockfile (commit this)
├── .venv/                               ← virtual env (DO NOT commit; in .gitignore)
└── .python-version                      ← pins Python version (optional, commit this)
```

---

## 📚 References

- **`uv` install docs** — https://docs.astral.sh/uv/getting-started/installation/
- **Hynek Schlawack's "uv tutorial"** — https://hynek.me/articles/python-uv/
- **"Astral's vision"** — https://astral.sh/blog/uv

---

## ✅ Exit criteria for this lesson

- [ ] `uv --version` prints a version
- [ ] `uv python install 3.12` completed without errors
- [ ] `uv python list` shows a `3.12.x` entry
- [ ] I understand `uv` is replacing `pip + venv + pyenv + pip-tools` in one binary

**Next:** [`02-project-skeleton.md`](02-project-skeleton.md) — create the actual project.

---

🌀 *Magic applied with Wibey VS Code Extension 🪄*
