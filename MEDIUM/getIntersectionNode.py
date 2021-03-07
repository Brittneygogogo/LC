class Solution:
    def getIntersectionNode(self, headA, headB):
        curr1, curr2 = headA, headB
        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA

        return curr1