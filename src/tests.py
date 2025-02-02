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
    
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
#        self.assertEqual(
#            m1._cells[0][0].has_top_wall,
#            False,
#        )
#        self.assertEqual(
#            m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall,
#            False,
#        )

    def test_exit_random(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m2 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m3 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m4 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m5 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        print(f"---PRINT---")
        


    def test_visited_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEquals(
            m1._cells[0][3].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()