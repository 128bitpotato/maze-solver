from graphics import Window, Line, Point
from constants import *
from cell import Cell
from maze import Maze
import sys

def main():
    num_rows = NUM_ROWS
    num_cols = NUM_COLS
    margin = CELL_MARGIN
    screen_x = SCREEN_WIDTH
    screen_y = SCREEN_HEIGHT

    # cell size to fit screen
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solvable = maze.solve()
    if not is_solvable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()

if __name__ == "__main__":
    main()