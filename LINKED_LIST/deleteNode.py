'''
定义一个函数删除该节点。
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur:
            pre.next = cur.next
        return head


s = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)

print(s.deleteNode(root, 3))