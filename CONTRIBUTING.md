# Contributing to A2A-Protocol

Thanks for wanting to contribute! This document explains the recommended developer workflow and one-line commands to run common tasks locally.

## Quick setup
1. Clone the repo and enter the project root.
2. Create and activate a virtual environment (recommended).
3. Install runtime + dev dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

## Common tasks
- Run tests:

```bash
pytest -q
```

- Run the example:

```bash
python -m examples.research_agent
```

- Lint the code:

```bash
flake8 .
```

## Branches and PRs
- Create a topic branch from `main` named `feature/<short-descriptive-name>` or `fix/<short-description>`.
- Open a Pull Request against `main`. Use the PR template provided.
- CI will run lint and tests automatically via GitHub Actions.

## Filing issues
- Use the repository Issues tab. Provide a clear title, reproduction steps and expected vs actual behavior.

## Release & Publishing
- Bump `version` in `pyproject.toml`, tag the commit (`git tag vX.Y.Z`) and push tags.
- Create a GitHub Release from the tag — the `python-publish` workflow handles publishing to PyPI if `PYPI_API_TOKEN` is configured.

## Code style
- Keep lines under 127 chars (flake8 configured).
- Follow idiomatic Python and add type hints where helpful.

---

If you need help with any of the steps above, open an issue or mention @GlobalAgents-Hub in a PR discussion.