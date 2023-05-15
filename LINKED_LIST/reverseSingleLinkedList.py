# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
递归
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head==None or head.next== None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
    

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev


root = ListNode(1)
root.next  = ListNode(2)
root.next.next  = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
#

x = Solution()
#新链表头结点， 原链表尾结点
print(x.reverseList(root).val)