
# 这段代码首先是一个迭代，从1到nums的最后一个数字(range这个函数不懂的可以查一下)，
# 然后就是总体了,nums[i]是从1开始的，开始算的是num[0]+nums[1]与nums[i]的最大值，
# 这里这么写可以看成nums[i-1]+nums[i]是看nums[i-1]大于0还是小于0，大于0自然选这个，
# 小于0的话，相加是要比num[i]小的，所以选择num[i]，这样一直往后迭代，最后返回max(nums),
# 也就是nums列表的最大值。


def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i])
    return max(nums)



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        # base case
        # 第一个元素前面没有子数组
        dp[0] = nums[0]
        # 状态转移方程
        for i in range(1, n):
            dp[i] = max(nums[i], nums[i] + dp[i - 1])
        # 得到 nums 的最大子数组
        res = float('-inf')
        for i in range(n):
            res = max(res, dp[i])
        return res



print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))