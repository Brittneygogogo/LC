class Solution:
    def maxProduct(self, nums):
        maxF = nums[0]
        minF = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            maxF = max(maxF * nums[i], nums[i], minF * nums[i])
            minF = min(minF * nums[i], nums[i], maxF * nums[i])
            ans = max(maxF, ans)
        return ans

x = Solution()
print(x.maxProduct([2,3,-2,4]))
print(x.maxProduct([-2,0,-1]))