# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def reverseKGroup(head: ListNode, k: int):
    #dummy是伪节点，作为总体的头结点
    dummy = ListNode(0)
    p = dummy
    while True:
        count = k
        stack = []
        #tmp和head都是每轮的第一个节点,tmp用来移动往后数count个数。head为当前轮的第一个节点
        tmp = head
        while count and tmp:
            stack.append(tmp)
            tmp = tmp.next
            count -= 1
        # 注意,目前tmp所在k+1位置
        # 说明剩下的链表不够k个,跳出循环
        if count:
            p.next = head
            break
        # 翻转操作，p为每轮翻转前的头结点，因此指向翻转后的第一个节点
        while stack:
            p.next = stack.pop()
            p = p.next
        #此时p为stack中的最后一个节点，与剩下链表连接起来
        p.next = tmp
        #重新数第二轮count的时候，tmp和head仍然指向第一个节点
        head = tmp
    return dummy.next

l1 = ListNode(1, next = ListNode(2, next = ListNode(3, next=ListNode(4, next = ListNode(5)))))

# while l1 != None:
#     print(l1.val)
#     l1 = l1.next

l2 = reverseKGroup(l1, 3)
#
while l2 != None:
    print(l2.val)
    l2 = l2.next

