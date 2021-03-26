# coding=utf-8

# class Solution:
def maxcost(matrix, max_cost, start_row, start_col):
    print(start_row, start_col)
    if start_row == m - 1 and start_col == n - 1:
        return True
    if start_col + 1 < n:
        if abs(matrix[start_row][start_col + 1] - matrix[start_row][start_col]) <= max_cost:
            return maxcost(matrix, max_cost, start_row, start_col + 1)
    if start_row + 1 < n:
        if abs(matrix[start_row + 1][start_col] - matrix[start_row][start_col]) <= max_cost:
            return maxcost(matrix, max_cost, start_row + 1, start_col)
    return False


# s = Solution()
matrix = [[2, 4, 6],
          [5, 7, 9],
          [1, 8, 8]]
m = len(matrix)
n = len(matrix[0])
print(maxcost(matrix, 3, 0, 0))