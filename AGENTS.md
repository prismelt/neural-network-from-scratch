# Contributor and Coding Agent Guide

## Project purpose

This repository teaches neural network fundamentals to beginners through explanations, visual materials, and a from-scratch Python implementation. Keep code and documentation approachable, accurate, and connected to the learning goals.

## General working practices

- Inspect the existing project structure and conventions before making changes.
- Keep changes focused and preserve established behavior unless the task calls for changing it.
- Prefer clear, direct implementations over unnecessary abstractions or dependencies.
- Update relevant documentation when setup, behavior, or project structure changes.
- Do not claim that commands or checks passed unless they were run and their results were observed.

## Python style

- Choose meaningful, descriptive variable and function names, even when they are long. Avoid contractions and cryptic abbreviations so beginner readers can understand the code.
- Add type annotations to function parameters, return values, and variables where they clarify what the code represents. Use appropriate types consistently rather than leaving important values ambiguous.
- Avoid inline `#` comments that interrupt the flow of code. Put a module docstring at the beginning of each Python file and a docstring on each function and class. Explain the purpose, inputs, outputs, and the meaning of important parameters or values in those docstrings. Use inline comments only when a specific detail cannot be explained clearly in a docstring.
- Keep functions small and name them according to the work they perform.
- Explain mathematical notation and algorithm steps in teaching material as well as in code documentation where helpful.

## Notebooks and learning materials

- Present concepts in a progression suitable for beginners. Introduce notation before relying on it.
- Use Markdown cells to explain the idea, then use diagrams or code examples to make it concrete.
- Keep notebook examples runnable and focused. Avoid duplicating the full implementation when a notebook can import and demonstrate code from the package.
- Store notebook images and supporting media in the project assets directory, using stable relative paths.
- Keep notebook outputs relevant and avoid committing unnecessary large outputs.

## Tests and verification

- Keep pytest tests current when implementation behavior changes. Add or update tests for new behavior and bug fixes.
- Run the relevant tests with `uv run pytest` after Python changes when the environment and dependencies are available.
- If tests cannot be run, report the reason clearly and identify what remains unverified.
- Keep tests readable and descriptive so they also help teach expected behavior.

## Dependencies and data

- Manage Python dependencies with uv and keep `pyproject.toml` and `uv.lock` consistent.
- Add dependencies only when they support a clear project need; explain optional or substantial dependencies in the README.
- Record the origin and license of external datasets and media. Do not commit large generated or downloaded data unless the project explicitly requires it.
