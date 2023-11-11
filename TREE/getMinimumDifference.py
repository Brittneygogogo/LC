'''
全部用self变量， 递归不能用全局变量

https://leetcode.cn/problems/minimum-absolute-difference-in-bst/solutions/2491572/javapython3czhong-xu-bian-li-ji-lu-sheng-g9rf/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if self.pre == -1:
            self.pre = root.val
        else:
            self.ans = min(self.ans, root.val - self.pre)  # 后遍历的节点一定大于先遍历，因此直接做差即可
            self.pre = root.val
        self.dfs(root.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.pre = -1
        self.ans = 1000
        self.dfs(root)
        return self.ans
