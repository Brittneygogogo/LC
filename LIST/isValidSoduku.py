'''如board[2][2]一定是第0个box，board[4][7]一定是第5个box，

而对于9x9的矩阵，我们光根据j/3得到0/1/2还是不够的，可能加上一个3的倍数，例如加0x3,表示本行的box，加1x3，表示在下一行的box，加2x3，表示在下两行的box， 这里的0/1/2怎么来的？和j/3差不多同理，也就是i/3。
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        block = [[0] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    b = (i // 3) * 3 + j // 3
                    if row[i][num] or col[j][num] or block[b][num]:
                        return False
                    row[i][num] = col[j][num] = block[b][num] = 1
        return True

