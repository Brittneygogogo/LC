# 堆排序的思想
'''
可借助python中的heapq模块实现堆的功能, 注意建立的是小根堆
'''
# class Solution1:
#     def findKthLargest(self, nums, k: int) -> int:
#         import heapq as hq
#         heap = []
#         for i in nums:
#             hq.heappush(heap, i)
#             if len(heap) > k:
#                 hq.heappop(heap)
#         return heap[0]
#
# 自己实现堆
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_idx = idx
            if left < max_len and nums[max_idx] < nums[left]:
                max_idx = left
            if right < max_len and nums[max_idx] < nums[right]:
                max_idx = right
            if max_idx != idx:
                nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
                adjust_heap(max_idx, max_len)

        # 建堆
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        # print(nums)
        res = None
        for i in range(1, k + 1):
            # print(nums)
            res = nums[0]
            nums[0], nums[-i] = nums[-i], nums[0]
            adjust_heap(0, n - i)
        return res

x = Solution()
print(x.findKthLargest([3,2,1,5,6,4], k = 2))
print(x.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))