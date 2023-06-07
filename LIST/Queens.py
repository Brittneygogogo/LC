# 注意：python 代码由 chatGPT🤖 根据我的 cpp 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for j in range(n)] for i in range(n)]  # 初始化空棋盘
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board: List[List[str]], row: int):
        if row == len(board):  # 触发结束条件
            self.res.append([''.join(board[i]) for i in range(len(board))])
            return

        for col in range(len(board[row])):
            if not self.isValid(board, row, col):  # 排除不合法选择
                continue
            board[row][col] = 'Q'  # 做选择
            self.backtrack(board, row + 1)  # 进入下一行决策
            board[row][col] = '.'  # 撤销选择

    def isValid(self, board: List[List[str]], row: int, col: int) -> bool:
        n = len(board)
        # 检查列是否有皇后互相冲突
        for i in range(row + 1):
            if board[i][col] == 'Q':
                return False
        # 检查右上方是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        # 检查左上方是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
# 详细解析参见：
# https://labuladong.github.io/article/?qno=51
