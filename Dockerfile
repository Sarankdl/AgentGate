FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project
COPY src ./src
EXPOSE 8000
CMD ["uv", "run", "--no-sync", "uvicorn", "agentgate.main:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "8000"]
