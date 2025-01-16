import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(10, 10, num_rows * 3, num_cols * 5, 15, 15)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_rows * 3
        )
        self.assertEqual(
            len(m2._cells), 
            num_cols * 5
        )


if __name__ == "__main__":
    unittest.main()