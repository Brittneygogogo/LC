'''
通过后序和中序遍历结果构造二叉树

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # 存储 inorder 中值到索引的映射
        self.valToIndex = {}

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        for i in range(len(inorder)):
            self.valToIndex[inorder[i]] = i
        return self.build(inorder, 0, len(inorder) - 1,
                          postorder, 0, len(postorder) - 1)

    '''
    定义：
    中序遍历数组为 inorder in [inStart..inEnd]，
    后序遍历数组为 postorder  [postStart..postEnd] post，
    构造这个二叉树并返回该二叉树的根节点
    '''
    def build(self, inorder: List[int], inStart: int, inEnd: int,
              postorder: List[int], postStart: int, postEnd: int) -> TreeNode:

        if inStart > inEnd:
            return None
        # root 节点对应的值就是后序遍历数组的最后一个元素
        rootVal = postorder[postEnd]
        # rootVal 在中序遍历数组中的索引
        index = self.valToIndex[rootVal]
        # 左子树的节点个数
        leftSize = index - inStart
        root = TreeNode(rootVal)

        # 递归构造左右子树

        #注意后序的left size要-1
        root.left = self.build(inorder, inStart, index - 1,
                               postorder, postStart, postStart + leftSize - 1)

        root.right = self.build(inorder, index + 1, inEnd,
                                postorder, postStart + leftSize, postEnd - 1)
        return root
# 详细解析参见：
# https://labuladong.github.io/article/?qno=
