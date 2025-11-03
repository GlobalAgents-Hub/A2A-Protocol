"""
Examples package initializer.
This makes examples runnable via: python -m examples.research_agent
It ensures the `src` directory is on sys.path so `from a2a import ...` works without installing the package.
"""
import os
import sys

# Insert src to the front of sys.path so imports like `from a2a import ...` work
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC_PATH = os.path.join(REPO_ROOT, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)
