class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

'''
是否有环
https://leetcode.cn/problems/linked-list-cycle/solutions/440042/huan-xing-lian-biao-by-leetcode-solution/
fast 指针走过链表末端，说明链表无环，此时直接返回 null。

如果链表存在环，则双指针一定会相遇。因为每走 1轮，fast 与 slow 的间距 +1，fast 一定会追上 slow 


'''
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

'''
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。
https://leetcode.cn/problems/linked-list-cycle-ii/solutions/12616/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/?envType=study-plan-v2&envId=top-100-liked

都从头结点开始走，相遇后fast再从head走一遍相遇
'''
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
        return None


x = ListNode(2, None)
head = ListNode(0, ListNode(1, x))
x.next = ListNode(3, x)

s = Solution()
# print(s.hasCycle(head))
print(s.detectCycle(head))
