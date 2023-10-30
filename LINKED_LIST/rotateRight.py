class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
先将给定的链表连接成环，然后将指定位置断开。

具体代码中，我们首先计算出链表的长度 nnn，并找到该链表的末尾节点，将其与头节点相连。这样就得到了闭合为环的链表。然后我们找到新链表的最后一个节点（即原链表的第 (n−1)−(k mod n)(n - 1) - (k \bmod n)(n−1)−(kmodn) 个节点），将当前闭合为环的链表断开，即可得到我们所需要的结果。

特别地，当链表长度不大于 111，或者 kkk 为 nnn 的倍数时，新链表将与原链表相同，我们无需进行任何处理。


3是该删除的节点
1 -> 2 -> 3 -> 4 -> 5
         cur  ret
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        add = n - k % n
        if add == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret
