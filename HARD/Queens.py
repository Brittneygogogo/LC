'''
因为皇后是一行一行从上往下放的，所以左下方，右下方和正下方不用检查（还没放皇后）；因为一行只会放一个皇后，所以每行不用检查。也就是最后只用检查上面，左上，右上三个方向。
'''

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        self.backtrack(board, 0, n)
        return self.res

    def backtrack(self, board: List[List[str]], row: int, n:int) -> None:
        if row == len(board):
            self.res.append([row[:] for row in board])
            return

        for col in range(n):
            if not self.isValid(board, row, col, n):
                continue

            board[row][col] = "Q"
            self.backtrack(board, row + 1, n)
            board[row][col] = "."

    def isValid(self, board: List[List[str]], row: int, col: int, n:int) -> bool:
        # 检查列是否有皇后冲突
        for i in range(n):
            if board[i][col] == "Q":
                return False

        # 检查右上方是否有皇后冲突
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1

        # 检查左上方是否有皇后冲突
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        return True

x = Solution()
print(x.solveNQueens(4))