
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
        原链表为：head → 1 → 2 → 3 → 4 → null，
        要求链表为：head → 2 → 1 → 4 → 3 → null。
        ![](https://labuladong.github.io/pictures/kgroup/7.jpg)
"""


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        输入以 head 开头的单链表，将这个单链表中的每两个元素翻转，
        返回翻转后的链表头结点
        """
        if not head or not head.next:
            # 如果当前节点 head 为空, 或者下一个节点 head.next 为空, 将 head 直接返回
            return head
        # 定义三个变量, 分别为当前节点, 当前节点的下一个节点和下下个节点
        first, second, others = head, head.next, head.next.next
        # 先把前两个元素翻转
        second.next = first
        # 利用递归定义, 将剩下的链表节点两两翻转, 接到后面
        first.next = self.swapPairs(others)
        # 现在整个链表都成功翻转了, 返回新的头结点
        return second
