.PHONY: help install test lint format run dev docker-build docker-run k8s-deploy clean

ifneq (,$(wildcard ./.env))
include .env
export
endif

install-dev: ## Install dev dependencies
	uv sync --all-groups

install: ## Install production dependencies
	uv sync

test:
	uv run pytest

test-cov:
	uv run pytest --cov --cov-report=term-missing --cov-report=html

lint:
	uv run ruff check .
	uv run mypy domain application infrastructure main.py

format:
	uv run black .
	uv run ruff check --fix .

run:
	PYTHONPATH=src uv run uvicorn main:app --host 0.0.0.0 --port 8000

dev:
	PYTHONPATH=src uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload

docker-build:
	docker build -t api:latest .

docker-run: ## Run Docker container locally
	docker run --rm \
		--env-file .env \
		-p 8080:8080 \
		api:latest

clean: ## Clean up generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	rm -rf htmlcov .coverage

active-venv:
	@echo "To activate the virtual environment, run:"
	@echo "source .venv/bin/activate"