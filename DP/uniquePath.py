'''
https://leetcode.cn/problems/unique-paths/?envType=study-plan-v2&envId=top-100-liked
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #初始化1是因为第一行和第一列都是1，后面会改变值所以可以都初始化为1,[0][0]
        dp = [[1] * n] * m
        ans = 0
        # dp = [dp[i][0]==dp[0][]== for i in range(m) for j in range(j)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]

