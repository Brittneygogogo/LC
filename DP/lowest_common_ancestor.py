class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        ancestor = root
        while True:
            if p.val < ancestor.val and q.val < ancestor.val:
                ancestor = ancestor.left
            elif p.val > ancestor.val and q.val > ancestor.val:
                ancestor = ancestor.right
            else:
                break
        return ancestor

x = Solution
# print(x.lowestCommonAncestor())