.PHONY: run test lint format docker-build docker-run
run:
	uv run uvicorn agentgate.main:app --app-dir src --reload
test:
	uv run pytest
lint:
	uv run ruff check .
	uv run ruff format --check .
format:
	uv run ruff check --fix .
	uv run ruff format .
docker-build:
	docker build -t agentgate .
docker-run:
	docker run --rm -p 8000:8000 agentgate
