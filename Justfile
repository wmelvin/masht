@default:
  @just --list

@build: 
  uv build

@check:
  uv run ruff format --check

@clean:
  -rm dist/*
  -rmdir dist

@format:
  uv run ruff format

@lint:
  uv run ruff check

@test: 
  uv run pytest
