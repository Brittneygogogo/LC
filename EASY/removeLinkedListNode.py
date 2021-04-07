# '''
# 删除节点为val的所有节点
# '''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def removeElements(self, head: ListNode, val: int) -> ListNode:
#         sentinel = ListNode(0)
#         sentinel.next = head
#
#         prev, curr = sentinel, head
#         while curr:
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#                 curr = curr.next
#
#         return sentinel.next
#
#
#
# s = Solution()
# root = ListNode(1)
# root.next = ListNode(1)
# root.next.next = ListNode(1)
# print(s.removeElements(root, 1))