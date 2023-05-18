# Definition for singly-linked list.
from typing import List

'''
[[1, 2], [3, 7, 8], [4, 5, 6, 10]]
    0        1            2
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        que = []
        for index, node in enumerate(lists):
            if node != None:
                heapq.heappush(que, (node.val, index))

        dummy_node = ListNode(-1)
        cur = dummy_node
        while que:
            val, index = heapq.heappop(que)
            cur.next = lists[index]
            cur = cur.next
            lists[index] = lists[index].next
            if lists[index] != None:
                heapq.heappush(que, (lists[index].val, index))
        return dummy_node.next


