# GreenLevel HS Coding Club: Introduction to Neural Networks and Machine Learning

An educational project for beginners learning neural network fundamentals, including neurons, layers, activation functions, loss, and training algorithms. The project uses Harrison Kinsley and Daniel Kukiela's _Neural Networks from Scratch in Python_ as a reference.

## Project goals

The objective of this project is to break down the seeming extremely topic: **Neural Network** and **Machine Learning**. We wish to delineate the underlying concepts and clarify common misunderstandings by constructing mathematical operations and algorithms from scratch. We are dedicated to make this experience consumable, engaging, and rewarding for anyone wishing to embark on this journey.

## Start locally

From the project directory, sync the project environment and launch JupyterLab:

```bash
uv sync
uv run jupyter lab
```

Open a lesson notebook from `notebooks/` in the JupyterLab page. The notebook lessons are planned; until they are added, the Python package is under development in `src/neural_network/`.

## Project layout

```text
.
├── README.md
├── AGENTS.md
├── pyproject.toml
├── uv.lock
├── notebooks/             # Explanations, images, and executable lessons
├── src/
│   └── neural_network/    # From-scratch Python implementation
├── tests/                 # Pytest tests for the implementation
├── data/                  # Data used in lessons and examples
├── assets/                # Images and other notebook source materials
├── examples/              # Standalone demonstrations
└── docs/                  # Documentations
```

The package currently lives in `src/neural_network/`. Other directories in the layout are intended homes for the project materials as they are added. Keep large downloaded or generated datasets out of version control unless needed; document dataset sources and licenses in `data/README.md`.

## Run tests

Run the test suite from the project directory:

```bash
uv run pytest
```

Add or update pytest tests when implementation behavior changes. Tests and dependencies are still being established in this early project, so this command may not have tests to run yet.

## Development notes

Use uv to manage project dependencies. Add a runtime dependency with `uv add <package>` or a development dependency with `uv add --dev <package>`, then keep `pyproject.toml` and `uv.lock` in sync. The project currently has no runtime dependencies.

To install uv, follow the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/). JupyterLab should be added as a development dependency when notebook work begins:

```bash
uv add --dev jupyterlab
```

## Citations

_Harrison Kinsley & Daniel Kukiela. Neural Network from Scratch (NNFS) . https://nnfs.io_
