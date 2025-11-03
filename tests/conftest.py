import pytest

# This autouse fixture isolates file-based state for tests by switching the
# working directory to a fresh temporary directory for each test. Any code
# that reads/writes `data.json` (or other files) will operate inside this
# temporary directory and will not modify the repository root.

@pytest.fixture(autouse=True)
def isolate_data_file(tmp_path, monkeypatch):
    """Change cwd to a temp directory for each test to avoid polluting repo files."""
    monkeypatch.chdir(tmp_path)
    yield
    # tmp_path is removed automatically by pytest; nothing else to clean up.
