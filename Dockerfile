FROM python:3.13.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /app
# allows us to run python without "uv run"
ENV PATH=/app/.venv/bin:$PATH

COPY pyproject.toml .python-version uv.lock ./

# sync dependencies from uv.lock
RUN uv sync --locked

# COPY pipeline.py .
COPY ingest_data.py .

# ENTRYPOINT ['uv', 'run', 'python', 'pipeline.py']
ENTRYPOINT ["python", "ingest_data.py"]