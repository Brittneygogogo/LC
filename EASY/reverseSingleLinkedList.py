# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if (head==None or head.next== None):
            return head
        
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
    
'''
class Solution:
    def reverseList(self, head):
        prev = head
        curr = None
        while (prev != None):
            next = prev.next
            prev.next = curr
            curr = prev
            prev = next

        return curr




root = ListNode(1)
root.next  = ListNode(2)
root.next.next  = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
#
# while(root):
#     print(root.val)
#     root = root.next

x = Solution()
#新链表头结点， 原链表尾结点
print(x.reverseList(root).val)