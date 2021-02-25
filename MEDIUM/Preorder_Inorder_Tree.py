'''
通过前序和中序遍历结果构造二叉树
void traverse(TreeNode root) {
    // 前序遍历
    preorder.add(root.val);
    traverse(root.left);
    traverse(root.right);
}
void traverse(TreeNode root) {
    traverse(root.left);
    // 中序遍历
    inorder.add(root.val);
    traverse(root.right);
}
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    return build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

def build(preorder, preStart, preEnd, inorder, inStart, inEnd):
    rootVal = preorder[preStart]
    index = 0
    for i in range(inStart, inEnd):
        if inorder[i] == rootVal:
            index = i
            break
        i += 1

    leftSize = index - inStart
    root =  TreeNode(rootVal)

    root.left = build(preorder, preStart + 1, preStart + leftSize,
                      inorder, inStart, index - 1)

    root.right = build(preorder, preStart + leftSize + 1, preEnd,
                       inorder, index + 1, inEnd)
    return root