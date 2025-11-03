# PowerShell helper for common development tasks
param(
    [string]$task = "help"
)

switch ($task) {
    "install-dev" {
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install -e .
        break
    }
    "test" {
        pytest -q
        break
    }
    "lint" {
        flake8 . --max-line-length=127
        break
    }
    "run-example" {
        python -m examples.research_agent
        break
    }
    default {
        Write-Host "Usage: .\scripts\dev.ps1 <install-dev|test|lint|run-example>"
    }
}
