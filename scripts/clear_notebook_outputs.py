"""
Clear saved execution results from Jupyter notebooks in this project.

Execute this file by running

```bash
uv run scripts/clear_notebook_outputs.py
```
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

PROJECT_DIRECTORY = Path(__file__).resolve().parent.parent
DEFAULT_NOTEBOOK_DIRECTORY = PROJECT_DIRECTORY / "notebooks"


def collect_notebooks(paths: Sequence[Path]) -> list[Path]:
    """Find notebooks under the supplied files or directories.

    Relative paths are interpreted from the project root. When no paths are
    supplied, all notebooks under the project's notebooks directory are used.
    """
    requested_paths = list(paths) or [DEFAULT_NOTEBOOK_DIRECTORY]
    notebook_paths: set[Path] = set()

    for requested_path in requested_paths:
        resolved_path = requested_path
        if not resolved_path.is_absolute():
            resolved_path = PROJECT_DIRECTORY / resolved_path

        if resolved_path.is_dir():
            notebook_paths.update(resolved_path.rglob("*.ipynb"))
        elif resolved_path.is_file() and resolved_path.suffix == ".ipynb":
            notebook_paths.add(resolved_path)
        else:
            raise FileNotFoundError(f"Notebook path does not exist: {resolved_path}")

    return sorted(notebook_paths)


def clear_notebook(path: Path, check_only: bool) -> bool:
    """Clear execution outputs and counts in one notebook.

    Return whether the notebook contains saved execution state. In check-only
    mode, inspect without writing changes.
    """
    notebook_text = path.read_text(encoding="utf-8")
    notebook = json.loads(notebook_text)
    changed = False

    for cell in notebook.get("cells", []):
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

        cell_metadata = cell.get("metadata", {})
        if "execution" in cell_metadata:
            del cell_metadata["execution"]
            changed = True

    notebook_metadata = notebook.get("metadata", {})
    if "widgets" in notebook_metadata:
        del notebook_metadata["widgets"]
        changed = True

    if changed and not check_only:
        cleaned_text = json.dumps(notebook, ensure_ascii=False, indent=2) + "\n"
        path.write_text(cleaned_text, encoding="utf-8")

    return changed


def main(arguments: Sequence[str] | None = None) -> int:
    """Clear notebooks, or report whether any saved execution state remains."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report notebooks with saved outputs without modifying them.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        help="Notebook files or directories, relative to the project root.",
    )
    options = parser.parse_args(arguments)
    notebook_paths = collect_notebooks(options.paths)

    notebooks_with_outputs = [
        path for path in notebook_paths if clear_notebook(path, options.check)
    ]

    if options.check:
        if notebooks_with_outputs:
            print("Notebooks contain saved outputs or execution counts:")
            for notebook_path in notebooks_with_outputs:
                print(f"- {notebook_path.relative_to(PROJECT_DIRECTORY)}")
            return 1
        print(f"Checked {len(notebook_paths)} notebooks; all are clean.")
        return 0

    if notebooks_with_outputs:
        for notebook_path in notebooks_with_outputs:
            print(f"Cleared outputs: {notebook_path.relative_to(PROJECT_DIRECTORY)}")
    else:
        print(f"Checked {len(notebook_paths)} notebooks; all are already clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
