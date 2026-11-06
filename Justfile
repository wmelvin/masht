@default:
  @just --list

@build: lint check test
  uv build

@check:
  uv run ruff format --check

@clean:
  -rm dist/*

@format:
  uv run ruff format

@lint:
  uv run ruff check

@test: 
  uv run pytest

@tox:
  uv run tox
