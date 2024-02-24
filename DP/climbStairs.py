'''
青蛙跳台阶问题： f(0)=1f(0)=1f(0)=1 , f(1)=1f(1)=1f(1)=1 , f(2)=2f(2)=2f(2)=2 。
斐波那契数列问题： f(0)=0f(0)=0f(0)=0 , f(1)=1f(1)=1f(1)=1 , f(2)=1f(2)=1f(2)=1 。

2级台阶是0， 1， 2
如n=2，dp需要n+1包括2
'''

class Solution:
    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

x = Solution()

print(x.climbStairs(3))
