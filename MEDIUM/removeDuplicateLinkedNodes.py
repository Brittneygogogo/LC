class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
重复出现一次
'''
# class Solution:
#     def deleteDuplicates(self, head):
#         if not head:
#             return head
#
#         cur = head
#         while cur.next:
#             if cur.val == cur.next.val:
#                 cur.next = cur.next.next
#             else:
#                 cur = cur.next
#
#         return head

'''
重复的不出现
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


s = Solution()
root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
print(s.deleteDuplicates(root))