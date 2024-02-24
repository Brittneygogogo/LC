from typing import List
'''
https://leetcode.cn/problems/median-of-two-sorted-arrays/solutions/258842/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/?company_slug=bytedance
要找到第 k 个元素，我们可以比较 A[k/2−1]  和 B[k/2−1]
如果比k/2 -1 小 那么肯定比k小
'''
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         def getKthElement(k):
#             """
#             - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
#             - 这里的 "/" 表示整除
#             - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
#             - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
#             - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
#             - 这样 pivot 本身最大也只能是第 k-1 小的元素
#             - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
#             - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
#             - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
#             """

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKth(k):
            index1, index2 = 0, 0
            while True:
                if index1 == len1:
                    return nums2[index2 + k - 1]
                if index2 == len2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newindex1 = min(index1 + k // 2 - 1, len1 - 1)
                newindex2 = min(index2 + k // 2 - 1, len2 - 1)
                pivot1, pivot2 = nums1[newindex1], nums2[newindex2]
                if pivot1 <= pivot2:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 - index2 + 1
                    index2 = newindex2 + 1

        len1 = len(nums1)
        len2 = len(nums2)
        t = len1 + len2
        if t % 2 == 1:
            return getKth(t//2 + 1)
        else:
            return (getKth(t//2) + getKth(t//2 + 1)) / 2

x = Solution()
print(x.findMedianSortedArrays([1,3,4,9], [1,2,3,4,5,6,7,8,9]))