
'''
https://leetcode.cn/problems/coin-change/solutions/132979/322-ling-qian-dui-huan-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

'''
https://labuladong.gitee.io/algo/di-er-zhan-a01c6/dong-tai-g-a223e/dong-tai-g-1e688/
'''

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [amount + 1] * (amount + 1)
#         # 数组大小为 amount+1，初始值也为 amount+1
#         dp[0] = 0
#         # base case
#         # 初始值为0
#         # 外层 for 循环在遍历所有状态的所有取值
#         for i in range(len(dp)):
#             # 内层 for 循环在求所有选择的最小值
#             for coin in coins:
#                 # 子问题无解，跳过
#                 if i - coin < 0:
#                     continue
#                 dp[i] = min(dp[i], 1 + dp[i - coin])
#
#                 # 如果结果是初始值，则表示没有找到解。
#         return -1 if dp[amount] == amount + 1 else dp[amount]


# print(coinChange([1,2,5], 11))
print(coinChange([1,2,5], 11))


class Solution:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        rec = [[0] * (n + 2) for _ in range(n + 2)]
        val = [1] + nums + [1]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    total = val[i] * val[k] * val[j]
                    total += rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)

        return rec[0][n + 1]


class Solution:
    def maxCoins(self, nums) -> int:

        #nums首尾添加1，方便处理边界情况
        nums.insert(0,1)
        nums.insert(len(nums),1)

        store = [[0]*(len(nums)) for i in range(len(nums))]

        def range_best(i,j):
            m = 0
            #k是(i,j)区间内最后一个被戳的气球
            for k in range(i+1,j): #k取值在(i,j)开区间中
                #以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i]*nums[k]*nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        #对每一个区间长度进行循环
        for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
            #开区间长度会从3一直到len(nums)
            #因为这里取的是range，所以最后一个数字是len(nums)-1

            #对于每一个区间长度，循环区间开头的i
            for i in range(0,len(nums)-n): #i+n = len(nums)-1

                #计算这个区间的最多金币
                range_best(i,i+n)

        return store[0][len(nums)-1]

