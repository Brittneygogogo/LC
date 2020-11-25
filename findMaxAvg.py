'''

相比于创建一个累加和数组，再遍历计算最大平均值，本方法只需要遍历一次数组 num，从中找出长度为 k 的子数组最大和。

假设我们已经索引从 i 到 i+k 子数组和为 x。要知道索引从 i+1 到 i+k+1 子数组和，
只需要从 x 减去 sum[i]，加上 sum[i+k+1] 即可。
根据此方法可以获得长度为 k 的子数组最大平均值。


'''
class Solution :
    def findMaxAverage(self, nums, k):
        sum=0
        i = 0
        while i < k:
            sum += nums[i]
            i += 1
        res = sum
        i = k
        while i < len(nums):
            sum += nums[i] - nums[i-k]
            res = max(res, sum)
            i += 1
        return res/k


x = Solution()
print(x.findMaxAverage([1,12,-5,-6,50,3], 4))