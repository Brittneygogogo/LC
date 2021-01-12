'''
但是在实际递推中我们发现，计算 dp[i][j]时，只用到了下一行的 dp[i + 1][j]和 dp[i + 1][j + 1]。

'''

#
# class Solution:
#     def minimumTotal(self, triangle) -> int:
#         n = len(triangle)
#         f = [[0] * n for _ in range(2)]
#         f[0][0] = triangle[0][0]
#
#         for i in range(1, n):
#             curr, prev = i % 2, 1 - i % 2
#             f[curr][0] = f[prev][0] + triangle[i][0]
#             for j in range(1, i):
#                 f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
#             f[curr][i] = f[prev][i - 1] + triangle[i][i]
#         return min(f[(n - 1) % 2])
#

# class Solution:
#     def minimumTotal(self, triangle) -> int:
#         n = len(triangle)
#         f = [0] * n
#         f[0] = triangle[0][0]
#
#         for i in range(1, n):
#             f[i] = f[i - 1] + triangle[i][i]
#             for j in range(i - 1, 0, -1):
#                 f[j] = min(f[j - 1], f[j]) + triangle[i][j]
#             f[0] += triangle[i][0]
#
#         return min(f)


class Solution:
    def minimumTotal(self, triangle) -> int:
        m = len(triangle)
        dp = [0] * (len(triangle[m - 1]) + 1)
        for i in range(m - 1, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
                print("i,j\t", i, j, triangle[i][j], dp)
        return dp[0]



x = Solution()
print(x.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
