'''
https://www.bilibili.com/video/BV18M411z7bb/?vd_source=7512af15cf008362a35e2a49d2b6bf68
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def dfs(node: Optional[TreeNode], depth: int) -> None:
        #     if node is None: return
        #     if depth == len(ans):
        #         ans.append(node.val)
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)
        # dfs(root, 0)
        # return ans

        if not root:
            return []
        ans = [root.val]
        while root.right:
            ans.append(root.right.val)
            root = root.right

        return ans