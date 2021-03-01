'''


nums2 中大于nums1的index
'''
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        res_dict = {i: -1 for i in nums2}
        for i in nums2:
            while stack and i > stack[-1]:
                small = stack.pop()
                res_dict[small] = i
            stack.append(i)
        res = []
        for j in nums1:
            res.append(res_dict[j])
        return res


# d = {}
# d.setdefault(1,1)

x = Solution()
print(x.nextGreaterElement([4,1,2], [1,3,4,2]))