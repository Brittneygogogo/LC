# class Solution:
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """

        # ans = []
        # n = len(nums2)
        # flag = False
        #
        # for e in nums1:
        #     indexOfe = nums2.index(e)
        #     for e2 in nums2[indexOfe + 1:]:
        #         if e2 > e:
        #             ans.append(e2)
        #             flag = True
        #             break
        #     if not flag:
        #         ans.append(-1)
        #     else:
        #         flag = False
        #
        # return ans

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


d = {}
d.setdefault(1,1)

x = Solution()
print(x.nextGreaterElement([4,1,2], [1,3,4,2]))