from cell import Cell
from constants import *
from time import sleep
import random
from constants import BUILD_TIME, SOLVE_TIME

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
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        
        self.seed = seed
        if seed != None:
            random.seed(seed)

        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        sleep(BUILD_TIME)
    
    def _animate_solve(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(SOLVE_TIME)
    
    def _break_entrance_and_exit(self):
        # Entrance
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        # Exit
        # Random bottom row or right column
        random_p = random.randrange(0, 1) # random number 0 or 1 for placement of exit

        # 0 = Bottom row
        if random_p == 0:
            exit_col = random.randrange(len(self._cells) - 1)
            exit_row = -1
        # 1 = Right column
        else:
            exit_col = -1
            exit_row = random.randrange(len(self._cells) // 2, len(self._cells) - 1)
        # Apply exit
        self._cells[exit_col][exit_row].has_bottom_wall = False
        self._draw_cell(exit_col, exit_row)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
        
            # Left
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j))
            # Up
            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1))
            # Right        
            if i < self._num_cols - 1:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j))
            # Down        
            if j < self._num_rows - 1:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1))
                    

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            # Randomly choose next direction to visit
            random_num = random.randrange(len(to_visit)) # Random num
            dir = to_visit.pop(random_num) # Direction

            # Left
            if dir[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[dir[0]][dir[1]].has_right_wall = False
            # Right
            if dir[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[dir[0]][dir[1]].has_left_wall = False
            # Up
            if dir[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[dir[0]][dir[1]].has_bottom_wall = False
            # Down
            if dir[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[dir[0]][dir[1]].has_top_wall = False
                
            # Recursivly call on next cell
            self._break_walls_r(dir[0], dir[1])

    def _reset_cells_visited(self):
        for list in self._cells:
            for cell in list:
                cell.visited = False

    def solve(self):
        solved = False
        while not solved:
            solved = self._solve_r()
        return solved

    def _solve_r(self, i=0, j=0):
        self._animate_solve()
        self._cells[i][j].visited = True

        if self._cells[i][j].exit == True:
            return True
        
        to_visit = []
        # Down        
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall:
            if not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
        # Right        
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall:
            if not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
        # Left
        if i > 0 and not self._cells[i][j].has_left_wall:
            if not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
        # Up
        if j > 0 and not self._cells[i][j].has_top_wall:
            if not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))


        while len(to_visit) != 0:
            next = to_visit.pop(0)
            self._cells[i][j].draw_move(self._cells[next[0]][next[1]])
            solved = self._solve_r(next[0], next[1])
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[next[0]][next[1]], undo=True)
        return False