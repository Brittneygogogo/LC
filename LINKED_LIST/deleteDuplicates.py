class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
1     ->     2     ->        3       ->   4  
cur       cur.next    cur.next.next
dummy
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


