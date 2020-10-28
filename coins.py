
"""
动态规划的核心问题是穷举。因为要求最值，肯定要把所有可行的答案穷举出来，然后在其中找最值呗。

给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。算法的函数签名如下：

// coins 中是可选硬币面值，amount 是目标金额
int coinChange(int[] coins, int amount);
比如说 k = 3，面值分别为 1，2，5，总金额 amount = 11。那么最少需要 3 枚硬币凑出，即 11 = 5 + 5 + 1。

你认为计算机应该如何解决这个问题？显然，就是把所有肯能的凑硬币方法都穷举出来，然后找找看最少需要多少枚硬币。

 为啥 dp 数组初始化为 amount + 1 呢，因为凑成 amount 金额的硬 币数最多只可能等于 amount (全用1元面值的硬币)，所以初始化为
 amount + 1 就相当于初始化为正无穷，便于后续取最小值。

每次遍历0-11的金钱数，每个金钱数再分别遍历每个coin，比较当前的coin数和+1哪个小，看能凑出来的最小coin数

"""
#自底向上
#dp 数组的定义：当目标金额为 i 时，至少需要 dp[i] 枚硬币凑出

def coinChange(coins, amount):
    # dp = len(amount)+1
    dp = list(range(12))
    # dp[0] = 0
    print(dp)
    for i in range(len(dp)):
        for coin in coins:
            if i -coin <0: continue
            dp[i] = min(dp[i], 1 + dp[i-coin])

    # if dp[amount] == amount+1:
    print(dp[amount])

    return -1
    return dp[amount]

#自顶向下，暴力遍历，dp(n) 的定义：输入一个目标金额 n，返回凑出目标金额 n 的最少硬币数量。
# 基础版，可加memo
# def coinChange1(coins, amount):
#     def dp(n):
#         if n == 0: return 0
#         if n < 0: return -1
#
#         res = float('INF')
#         for coin in coins:
#             subproblem = dp(n - coin)
#             # 子问题无解，跳过
#             if subproblem == -1: continue
#             res = min(res, 1 + subproblem)
#         return res if res != float('INF') else -1
#     return dp(amount)



# print(coinChange([1,2,5], 11))
print(coinChange1([1,2,5], 11))