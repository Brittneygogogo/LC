class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA and not headB:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa