class Solution:
    def matrixReshape(self, nums, r: int, c: int):
        m,n=len(nums),len(nums[0])
        if m*n!=r*c:
            return nums
        res=[i for j in nums for i in j]
        return [res[i:i+c] for i in range(0,len(res),c)]


x = Solution()

