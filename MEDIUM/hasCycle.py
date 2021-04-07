
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class Solution:
    def detectCycle(self, head: ListNode):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                fast = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return fast.val



x = ListNode(2, None)
head = ListNode(0, ListNode(1, x))
x.next = ListNode(3, x)

s = Solution()
# print(s.hasCycle(head))
print(s.detectCycle(head))
