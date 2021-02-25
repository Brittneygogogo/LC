'''
通过`后序和中序遍历结果构造二叉树

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(postorder, inorder):
    return build(postorder, 0, len(postorder)-1, inorder, 0, len(inorder)-1)

def build(postorder, poStart, poEnd, inorder, inStart, inEnd):
    rootVal = postorder[poStart]
    index = 0
    for i in range(inStart, inEnd):
        if inorder[i] == rootVal:
            index = i
            break
        i += 1

    leftSize = index - inStart
    root =  TreeNode(rootVal)

    root.left = build(postorder, poStart , poStart + leftSize - 1,
                      inorder, inStart, index - 1)

    root.right = build(postorder, poStart + leftSize, poEnd - 1,
                       inorder, index + 1, inEnd)
    return root