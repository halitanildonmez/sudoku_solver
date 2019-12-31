import unittest


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return -1, -1


def is_in_grid(grid, val):
    for row in grid:
        if val in row:
            return True
    return False


class SudokuSolver():

    def solve_board_backtack(self, bo):
        e_r, e_c = find_empty(bo)
        if e_r == -1 and e_c == -1:
            return True
        empty_row = bo[e_r]
        empty_col = [sub[e_c] for sub in bo]

        rr = int(e_r / 3) * 3
        cc = int(e_c / 3)

        g_c = [sub[cc * 3:cc * 3 + 3] for sub in bo[rr:rr + 3]]

        for r_c in range(1, 10):
            if r_c not in empty_row and r_c not in empty_col and is_in_grid(g_c, r_c) is False:
                bo[e_r][e_c] = r_c
                if self.solve_board_backtack(bo):
                    return True
        bo[e_r][e_c] = 0
        return False


class TestSudoku(unittest.TestCase):
    def test_solver(self):
        board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        expected_board = [
            [7, 8, 5, 4, 3, 9, 1, 2, 6],
            [6, 1, 2, 8, 7, 5, 3, 4, 9],
            [4, 9, 3, 6, 2, 1, 5, 7, 8],
            [8, 5, 7, 9, 4, 3, 2, 6, 1],
            [2, 6, 1, 7, 5, 8, 9, 3, 4],
            [9, 3, 4, 1, 6, 2, 7, 8, 5],
            [5, 7, 8, 3, 9, 4, 6, 1, 2],
            [1, 2, 6, 5, 8, 7, 4, 9, 3],
            [3, 4, 9, 2, 1, 6, 8, 5, 7]
        ]
        solver = SudokuSolver()
        solver.solve_board_backtack(board)
        self.assertEqual(board, expected_board)


if __name__ == '__main__':
    unittest.main()
