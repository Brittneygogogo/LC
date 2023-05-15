from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
 1   -> 2 -> 3 -> 4
head             last

'''
# 定义：输入一个单链表头节点，将该链表反转，返回新的头结点
def reverseLinkedList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    last = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return last
