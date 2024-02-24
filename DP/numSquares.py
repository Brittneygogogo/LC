'''
https://leetcode.cn/problems/perfect-squares/solutions/2498845/zui-rong-yi-li-jie-de-dong-tai-gui-hua-b-jcuj/?envType=study-plan-v2&envId=top-100-liked
因为有数组偏移 实际数字和平方数都需要从正数开始算，所以需要n + 1
'''
'''
按数值
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1,int(i**(0.5))+1):
                dp[i]=min(dp[i],dp[i-j*j] + 1)
        return dp[-1]


'''
dp
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 0, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 0, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 2, 0, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 0, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 0, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 0]
[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3]
'''
#只有数量
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [0]*(n + 1)
#         for i in range(1, n + 1):
#             dp[i] = min(dp[i - j * j] + 1 for j in range(1,int(i ** 0.5) + 1))
#             print(dp)
#         return dp[n]


#
# '''
# 1700ms
# '''
#
# class Solution:
#     def numSquares(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         for i in range(1, n + 1):
#             if i ** 0.5 % 1 == 0:
#                 dp[i] = 1
#             else:
#                 dp[i] = 1+min([dp[i-j*j] for j in range(1,int(i**0.5)+1)])
#         return dp[-1]


x = Solution()
print(x.numSquares(12))