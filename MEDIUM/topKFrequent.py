# 优先队列；n + nlogk， 时间复杂度： O(nlogk)
# 下面只从堆的角度考虑，从m个元素中，通过堆选出最大的k个数
# k大小的小根堆；堆满后，若新加的数大于堆首数，弹出堆首元素 -- 弹出了m-k个最小的
class Solution:
    def topKFrequent(self, nums, k:int):
        from collections import Counter
        import heapq as hq
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            # 如果堆满了（k个元素）
            if len(heap) == k:
                # 弹出最小频率的元组
                if heap[0][0] < freq:
                    hq.heapreplace(heap, (freq, num))
            else:
                hq.heappush(heap, (freq, num))
        while heap:
            res.append(hq.heappop(heap)[1])

        return res

x = Solution()
print(x.topKFrequent())