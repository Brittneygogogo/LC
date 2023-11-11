'''
螺旋矩阵
'''
from typing import List


class Solution:
    def printSpiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        l, r, t, b = 0, n - 1, 0, n - 1
        # mat = [[0 for _ in range(n)] for _ in range(n)]
        # num, tar = 1, n * n
        ans = []
        while l <= r and t <= b:
            for i in range(l, r + 1):  # left to right
                ans.append(matrix[l][i])
                # num += 1
            t += 1
            for i in range(t, b + 1):  # top to bottom
                ans.append(matrix[i][r])
                # num += 1
            r -= 1
            for i in range(r, l - 1, -1):  # right to left
                ans.append(matrix[b][i])
                # num += 1
            b -= 1
            for i in range(b, t - 1, -1):  # bottom to top
                ans.append(matrix[i][l])
                # num += 1
            l += 1
        return ans

    # def printSpiralOrder(self, matrix: List[List[int]]) -> List[int]:
    #     if not matrix: return []
    #     l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
    #     while True:
    #         for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
    #         t += 1
    #         if t > b: break
    #         for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
    #         r -= 1
    #         if l > r: break
    #         for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
    #         b -= 1
    #         if t > b: break
    #         for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
    #         l += 1
    #         if l > r: break
    #
    #     return res

# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return list()
#
#         rows, columns = len(matrix), len(matrix[0])
#         order = list()
#         left, right, top, bottom = 0, columns - 1, 0, rows - 1
#         while left <= right and top <= bottom:
#             for column in range(left, right + 1):
#                 order.append(matrix[top][column])
#             for row in range(top + 1, bottom + 1):
#                 order.append(matrix[row][right])
#             if left < right and top < bottom:
#                 for column in range(right - 1, left, -1):
#                     order.append(matrix[bottom][column])
#                 for row in range(bottom, top, -1):
#                     order.append(matrix[row][left])
#             left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
#         return order
matrix = [[1,2,3],[4,5,6],[7,8,9]]
x = Solution()
print(x.printSpiralOrder(matrix))