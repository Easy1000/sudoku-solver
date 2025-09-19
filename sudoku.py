import os
import click
import numpy

from digit_classification.get_model import get_digit_classification_model
from sudoku_detection.cells_puzzle import crop_cells, read_cells, splitcells
from sudoku_detection.contour_puzzle import contour
from sudoku_detection.load_puzzle import load_pzl_image
from sudoku_detection.threshold_puzzle import get_threshold
from sudoku_detection.wrap_puzzle import image_wrap
from sudoku_solver import solve_sudoku


@click.group()
def cli():
    pass


@cli.command()
@click.argument("filename")
def solve(filename: str):
    puzzle_img = load_pzl_image(f"./{filename}")
    threshold = get_threshold(puzzle_img)
    puzzle_contour = contour(threshold)
    puzzle_wrap = image_wrap(puzzle_contour, puzzle_img)
    sudoku_cells = splitcells(puzzle_wrap)
    sudoku_cells_cropped = crop_cells(sudoku_cells)
    model = get_digit_classification_model()
    puzzle = read_cells(sudoku_cells_cropped, model)
    puzzle = numpy.reshape(puzzle, (9, 9))
    os.system("clear")
    print("Sudoku puzzle being read:")
    print(puzzle)
    print()
    print("Sudoku puzzle solution:")
    solve_sudoku(puzzle)


if __name__ == "__main__":
    cli()
