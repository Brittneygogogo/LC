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

# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 存储 inorder 中值到索引的映射
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i

        return self.build(preorder, 0, len(preorder) - 1,
                          inorder, 0, len(inorder) - 1, valToIndex)

    def build(self, preorder, preStart, preEnd, inorder, inStart, inEnd, valToIndex):
        if preStart > preEnd:
            return None

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # rootVal 在中序遍历数组中的索引
        index = valToIndex[rootVal]

        leftSize = index - inStart

        # 先构造出当前根节点
        root = TreeNode(rootVal)

        # 递归构造左右子树
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               inorder, inStart, index - 1, valToIndex)

        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                inorder, index + 1, inEnd, valToIndex)
        return root
# 详细解析参见：
# https://labuladong.github.io/article/?qno=
