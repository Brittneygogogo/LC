class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

'''
删除重复出现一次的元素 ，只用curr， 从curr的值开始判断
'''

def deleteDuplicates1(head):
    if not head:
        return head

    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next

    return head



'''
只用一个指针curr
重复的全部删除
因为重复数字可能出现在第一个， 所以用dummy节点, 循环开始时cur = dummy ，最后返回dummy.next

1     ->     2     ->        3       ->   4  
cur       cur.next    cur.next.next
'''

class Solution:
    def deleteDuplicatesAll(self, head: ListNode) -> ListNode:
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
head = ListNode(1, ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, None))))))))


print(deleteDuplicates1(head).val)

# print(s.deleteDuplicatesAll(head).val)