from cell import Cell
from constants import *
from time import sleep

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._cells = []

        self._create_cells()

    def _create_cells(self):
        # Fill list with rows and rows with cells
        for column in range(self._num_cols):
            self._cells.append([])
            for cell in range(self._num_rows):
                self._cells[column].append(Cell(self._win))
        
        # Draw cell on each cell
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (self._cell_size_x * i)
        y1 = self._y1 + (self._cell_size_y * j)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.02)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].has_bottom_wall = False
        last_cell_col = len(self._cells)
        last_cell_row = len(self._cells[-1])
        self._draw_cell(last_cell_col, last_cell_row)

