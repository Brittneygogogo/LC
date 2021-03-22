# def climbStairs(n):
"""
:type n: int
:rtype: int
"""

class Solution:
    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

# def climbStairs(n):
#     p = 0
#     q = 0
#     r = 1
#     i = 1
#     while (i <= n):
#         i += 1
#         p = q
#         q = r
#         r = p + q
#     return r

x = Solution()

print(x.climbStairs(3))
