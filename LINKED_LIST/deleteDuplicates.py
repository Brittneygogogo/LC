class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
重复的不出现

1     ->     2     ->        3       ->   4  
cur       cur.next    cur.next.next
dummy       x
'''

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next

'''
重复出现一次
'''
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head



s = Solution()
root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
print(s.deleteDuplicates(root))