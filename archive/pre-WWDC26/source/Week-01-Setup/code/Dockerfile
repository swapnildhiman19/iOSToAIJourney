# 1. Base image: slim python 3.12
FROM python:3.12-slim

RUN pip install --no-cache-dir uv 

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY Day-01/self_hello_gemini.py ./

CMD ["uv", "run", "python", "self_hello_gemini.py"]