class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

x = Solution()
print(x.subsets([1,2,3]))