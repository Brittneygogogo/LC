'''
删除节点为val的所有节点
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
dummy -> head -> 1
prev     curr    1


另设dummy，以免头结点为删除节点。
两或多指针 从前往后依次传值
'''

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev, curr = dummy, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next


s = Solution()
root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
print(s.removeElements(root, 1))









