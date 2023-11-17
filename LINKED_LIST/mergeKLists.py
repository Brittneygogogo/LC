# Definition for singly-linked list.
from typing import List

'''
[[1, 2], [3, 7, 8], [4, 5, 6, 10]]
    0        1            2
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        que = []
        #每个列表在总列表里的位置，访问每个小列表都是直接访问头结点
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


ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n4 = ListNode(1)
n5 = ListNode(5)

n6 = ListNode(6)
n7 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = None

n4.next = n5
n5.next = None

n7.next = n6
n6.next = None

# [[1, 2, 3], [1, 5], [1, 6]]

l1 = n1
l2 = n4
l3 = n7

l = [l1, l2, l3]
x = Solution()

x.mergeKLists(l)
















