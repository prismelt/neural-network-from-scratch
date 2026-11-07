# GreenLevel HS Coding Club: Introduction to Neural Networks and Machine Learning

An educational project for beginners learning neural network fundamentals, including neurons, layers, activation functions, loss, and training algorithms. The project uses Harrison Kinsley and Daniel Kukiela's _Neural Networks from Scratch in Python_ as a reference.

## Project goals

The objective of this project is to break down the seeming extremely topic: **Neural Network** and **Machine Learning**. We wish to delineate the underlying concepts and clarify common misunderstandings by constructing mathematical operations and algorithms from scratch. We are dedicated to make this experience consumable, engaging, and rewarding for anyone wishing to embark on this journey.

## Start locally

From the project directory, sync the project environment using `uv`:

```bash
uv sync
```

You can launch and view jupyter notebooks directly in a coding editor such as `visual studio code`. You can also view them in the browser by running:

```bash
uv run jupyter lab
```

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

The `src` directory includes full implementations of neural networks and other algorithms. It consists implementations in `jax` and `numpy` from scratch. The `notebooks` directories includes notebooks with in-depth explanation of concepts, details, and code fragments in small, consumable pieces. Other directories serve purposes such as storing local datasets and benchmarking.

## Run tests

Run the test suite from the project directory:

```bash
uv run pytest
```

Tests and dependencies are still being established in this early project, so this command may not have tests to run yet.

## Development notes

Use uv to manage project dependencies. Add a runtime dependency with `uv add <package>` or a development dependency with `uv add --dev <package>`, then keep `pyproject.toml` and `uv.lock` in sync. The project currently has no runtime dependencies.

To install uv, follow the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/). JupyterLab should be added as a development dependency when notebook work begins:

```bash
uv add --dev jupyterlab
```

## Citations

_Harrison Kinsley & Daniel Kukiela. Neural Network from Scratch (NNFS) . https://nnfs.io_
