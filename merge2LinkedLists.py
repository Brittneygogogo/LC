
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


l1 = ListNode(1)
l1.next = ListNode(2, next=ListNode(4))

l2 = ListNode(1)
l2.next = ListNode(3, next=ListNode(4))

# while l1 != None:
#     print(l1.val)
#     l1 = l1.next
#
# while l2 != None:
#     print(l2.val)
#     l2 = l2.next


l = mergeTwoLists(l1,l2)
print()

while l!=None:
    print(l.val)
    l = l.next
