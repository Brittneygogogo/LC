class Solution:
    def findKthLargest(self, heap, k: int) -> int:
        def adjust_heap(idx, max_len):
            left = 2 * idx + 1
            right = 2 * idx + 2
            max_idx = idx
            if left < max_len and heap[max_idx] < heap[left]:
                max_idx = left
            if right < max_len and heap[max_idx] < heap[right]:
                max_idx = right
            if max_idx != idx:
                heap[idx], heap[max_idx] = heap[max_idx], heap[idx]
                adjust_heap(max_idx, max_len)

        # 建堆
        n = len(heap)
        for i in range(n // 2 - 1, -1, -1):
            adjust_heap(i, n)
        # print(heap)
        res = None
        for i in range(1, k + 1):
            # print(heap)
            res = heap[0]
            heap[0], heap[-i] = heap[-i], heap[0]
            adjust_heap(0, n - i)
        return res

x = Solution()
print(x.findKthLargest([3,2,1,5,6,4], k = 2))
print(x.findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))


'''
可借助python中的heapq模块实现堆的功能, 注意建立的是小根堆
'''
# class Solution1:
#     def findKthLargest(self, heap, k: int) -> int:
#         import heapq as hq
#         heap = []
#         for i in heap:
#             hq.heappush(heap, i)
#             if len(heap) > k:
#                 hq.heappop(heap)
#         return heap[0]
#
