# Sudoku Solver CLI App

CLI App to solve sudoku puzzle by image

## Installation

Currently, Sudoku Solver CLI provides a single prebuilt binary for **Linux**.

1. Go to the [Releases](https://github.com/Easy1000/sudoku-solver/releases) page.
2. Download the latest binary for linux.
3. Make it executable:

```bash
  chmod +x sudoku
```

4. Move it to a directory in your PATH, for example:

```bash
  sudo mv sudoku /usr/local/bin/
```

## Usage

```bash
  sudoku solve <sudoku-image-file>
```

For example:

```bash
  sudoku solve puzzle.jpg
```

This will display the solution in the terminal.
