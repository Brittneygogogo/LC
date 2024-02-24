from typing import List

'''
https://leetcode.cn/problems/minimum-path-sum/?envType=study-plan-v2&envId=top-100-liked
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        # dp = [[] * n ] * m
        dp = grid
        for i in range(m):
            for j in range(n):
                # if i == j == 0: continue
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        print(dp)
                # ans = min(dp[-1]), min(dp[-1][-1]))
        return dp[-1][-1]

x = Solution()
print(x.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))