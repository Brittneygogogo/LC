'''
对于任意一个位置 i，能够装的水为：
water[i] = min(
           # 左边最高的柱子
           max(height[0..i]),
           # 右边最高的柱子
           max(height[i..end])
        ) - height[i]

如何能够快速计算出某一个位置左侧所有柱子的最大高度和右侧所有柱子的最大高度。

这道题的解法比较多样，可以预计算数组，可以用 双指技巧，可以用单调栈技巧，这里就说一个最简单的解法，用预计算的方式求解，优化暴力解法的时间复杂度，
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        # 数组充当备忘录
        l_max = [0] * n
        r_max = [0] * n
        # 初始化 base case
        l_max[0] = height[0]
        r_max[n - 1] = height[n - 1]
        # 从左向右计算 l_max 从1开始
        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i - 1])
        # 从右向左计算 r_max
        for i in range(n - 2, -1, -1):
            r_max[i] = max(height[i], r_max[i + 1])
        # 计算答案
        for i in range(1, n - 1):
            res += min(l_max[i], r_max[i]) - height[i]

        return res