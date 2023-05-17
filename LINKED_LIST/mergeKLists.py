# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# class Solution:
#     def mergeKLists(self, lists) -> ListNode:
#         import heapq
#         dummy = ListNode(0)
#         p = dummy
#         head = []
#         for i in range(len(lists)):
#             if lists[i] :
#                 heapq.heappush(head, (lists[i].val, i))
#                 lists[i] = lists[i].next
#         while head:
#             val, idx = heapq.heappop(head)
#             p.next = ListNode(val)
#             p = p.next
#             if lists[idx]:
#                 heapq.heappush(head, (lists[idx].val, idx))
#                 lists[idx] = lists[idx].next
#         return dummy.next

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


