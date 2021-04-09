
memo = dict()
res = []

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def findDuplicateTrees(root):
    traverse(root)
    return res

def traverse(root):
    if root==None:
        return "#"
    left  = traverse(root.left)
    right = traverse(root.right)

    subTree = left+","+right+","+root.val
    freq = memo.setdefault(subTree,0)
    if freq ==1:
        res.append(root)
    memo[subTree] +=1
    return subTree