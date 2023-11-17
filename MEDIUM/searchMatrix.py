'''
https://leetcode.cn/problems/search-a-2d-matrix-ii/solutions/2361487/240-sou-suo-er-wei-ju-zhen-iitan-xin-qin-7mtf/?envType=study-plan-v2&envId=top-100-liked
其类似于 二叉搜索树  从左下找

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False


class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        m = len(matrix)
        n = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = m - 1
        col = 0

        while col < n and row >= 0:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
                print(matrix[row][col])

            else:  # found it
                return True

        return False





x = Solution()
print(x.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))