import unittest

# assuming your `Maze` class is in a file called `maze.py`
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 20
        num_rows = 15
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_small(self):
        num_cols = 3
        num_rows = 2
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_single_row(self):
        num_cols = 5
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_single_column(self):
        num_cols = 1
        num_rows = 7
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_square(self):
        num_cols = 8
        num_rows = 8
        m1 = Maze(0, 0, num_rows, num_cols, 15, 15)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_cells_are_cell_objects(self):
        """Test that the maze creates actual Cell objects"""
        from cell import Cell

        num_cols = 4
        num_rows = 3
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        # Check that each cell is actually a Cell object
        for i in range(num_cols):
            for j in range(num_rows):
                self.assertIsInstance(m1._Maze__cells[i][j], Cell)

        # Check that cells have the expected default wall configuration
        test_cell = m1._Maze__cells[0][0]
        self.assertTrue(test_cell.has_left_wall)
        self.assertTrue(test_cell.has_right_wall)
        self.assertTrue(test_cell.has_top_wall)
        self.assertTrue(test_cell.has_bottom_wall)


if __name__ == "__main__":
    unittest.main()
