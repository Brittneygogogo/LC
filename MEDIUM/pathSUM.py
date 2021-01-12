class Solution:
    def pathSum(self, root, sum):
        res = []
        if not root: return []

        def helper(root, sum, tmp):
            if not root:
                return
            if not root.left and not root.right and sum - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
                return
            helper(root.left, sum - root.val, tmp + [root.val])
            helper(root.right, sum - root.val, tmp + [root.val])

        helper(root, sum, [])
        return res


x = Solution()
# print(x.pathSum(root,))



class Solution:
    def pathSum(self, root, total: int):
        ret = list()
        path = list()

        def dfs(root, total):
            if not root:
                return
            path.append(root.val)
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path[:])
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()

        dfs(root, total)
        return ret


