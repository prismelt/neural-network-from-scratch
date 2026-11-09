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
├── notebooks/             # Lessons
├── src/neural_network/    # Package placeholder
├── scripts/               # Dataset preparation
├── data/                  # Small teaching datasets
└── assets/                # Notebook images
```

The first lesson is `notebooks/01-introduction-to-machine-learning.ipynb`. It fits a line and an exponential curve in plain Python. `src/neural_network` is a package placeholder; the from-scratch library is not implemented yet. `scripts/prepare_stock_data.py` rebuilds `data/google_stock_2025.csv`.

## Run tests

Run the test suite from the project directory:

```bash
uv run pytest
```

There are no tests yet, so pytest reports that none were collected.

## Development notes

Use uv to manage project dependencies. Add a runtime dependency with `uv add <package>` or a development dependency with `uv add --dev <package>`, then keep `pyproject.toml` and `uv.lock` in sync. Runtime dependencies are matplotlib, numpy, and pandas. The first notebook uses matplotlib and the Python standard library. JupyterLab and pytest are development dependencies.

To install uv, follow the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).

## Citations

_Harrison Kinsley & Daniel Kukiela. Neural Network from Scratch (NNFS) . https://nnfs.io_
