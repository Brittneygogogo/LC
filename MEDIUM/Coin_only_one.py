'''
有一个背包，容量为 sum，现在给你 N 个物品，第 i 个物品的重量为 nums[i - 1]（注意 1 <= i <= N），每个物品只有一个，请问你有几种不同的方法能够恰好装满这个背包？
如果不把 nums[i] 算入子集，或者说你不把这第 i 个物品装入背包，那么恰好装满背包的方法数就取决于上一个状态 dp[i-1][j]，继承之前的结果。
如果把 nums[i] 算入子集，或者说你把这第 i 个物品装入了背包，那么只要看前 i - 1 个物品有几种方法可以装满 j - nums[i-1] 的重量就行了，所以取决于状态 dp[i-1][j-nums[i-1]]。
注意我们说的 i 是从 1 开始算的，而数组 nums 的索引时从 0 开始算的，所以 nums[i-1] 代表的是第 i 个物品的重量，j - nums[i-1] 就是背包装入物品 i 之后还剩下的容量。
'''


'''
给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，最多能装的价值是多少？

举个简单的例子，输入如下：
N = 3, W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
算法返回 6，选择前两件物品装进背包，总重量 3 小于W，可以获得最大价值 6。
'''
def pack01(W, N, wt, val):
    dp = (N + 1) * [[0] * (W + 1)]
    for i in range(1, N + 1):
        for w in range(W, 0, -1):
            if w - wt[i - 1] < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w - wt[i - 1]] + val[i - 1],
                               dp[i - 1][w])
            # print(dp)
    return dp[N][W]

'''
减小空间复杂度
'''
# def pack01(W, N, wt, val):
#     dp = [0] * (W + 1)
#     for i in range(1, N + 1):
#         for w in range(W, 0, -1):
#             if w - wt[i] < 0:
#                 dp[w] = dp[w - 1]
#             else:
#                 dp[w] = max(dp[w - wt[i]] + val[i],
#                                dp[w])
#             print(dp)
#         return dp[W]


print(pack01(4, 3, [2, 1, 3], [4, 2, 3]))
# print(pack01([1, 2, 3], 6))
