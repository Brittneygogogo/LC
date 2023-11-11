# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l, r = root, root
        hl, hr = 0, 0
        # 记录左、右子树的高度
        while l:
            l = l.left
            hl += 1
        while r:
            r = r.right
            hr += 1
        # 如果左右子树的高度相同，则是一棵满二叉树
        if hl == hr:
            return 2 ** hl - 1
        # 如果左右高度不同，则按照普通二叉树的逻辑计算
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
# 详细解析参见：
# https://labuladong.github.io/article/?qno=

# class Solution {
# public int countNodes(TreeNode root) {
# if (root == null) {
#
#
# return 0;
# }
# int
# left = countNodes(root.left);
# int
# right = countNodes(root.right);
#
# return left + right + 1;
#
# }
# }