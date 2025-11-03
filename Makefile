# Simple Makefile for common development tasks
.PHONY: install-dev test lint run-example clean

install-dev:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .

test:
	pytest -q

lint:
	flake8 . --max-line-length=127

run-example:
	python -m examples.research_agent

clean:
	-find . -name "*.pyc" -delete
	-find . -name "__pycache__" -type d -exec rm -rf {} +
