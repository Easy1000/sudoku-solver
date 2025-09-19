import cv2


def load_pzl_image(puzzle_path: str):
    puzzle = cv2.imread(puzzle_path)
    puzzle = cv2.resize(puzzle, (450, 450))
    return puzzle
