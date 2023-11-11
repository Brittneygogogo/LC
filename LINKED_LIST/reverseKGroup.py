'''
https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/151616/di-gui-java-by-reedfan-2/?envType=study-plan-v2&envId=top-interview-150
22

找到待翻转的k个节点（注意：若剩余数量小于 k 的话，则不需要反转，因此直接返回待翻转部分的头结点即可）。
2、对其进行翻转。并返回翻转后的头结点（注意：翻转为左闭右开区间，所以本轮操作的尾结点其实就是下一轮操作的头结点）。
 3、对下一轮 k 个节点也进行翻转操作。
 4、将上一轮翻转后的尾结点指向下一轮翻转后的头节点，即将每一轮翻转的k的节点连接起来。

 1                k
 head             tail
 head..<-newhead  tail
 head = tail 继续循环
 head..<-newhead  head

1      2       3    4
head   cur          tail

pre
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reversed(self, head: ListNode, tail: ListNode):
        pre = None
        cur = None
        while head != tail:
            #找到下一个节点
            cur = head.next
            #反指指针pre
            head.next = pre
            #三指针都往前循环
            pre = head
            head = cur

        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        #tail 为k + 1
        tail = head
        for i in range(k):
            if tail == None:
                return head
            tail = tail.next

        newhead = self.reversed(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return newhead


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, None))))))))
newhead = solution.reverseKGroup(head, 3)
while newhead:
    print(newhead.val)
    newhead = newhead.next
