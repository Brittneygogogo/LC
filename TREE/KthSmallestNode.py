'''
BST 的中序遍历是升序序列。

那么回到这个问题，想找到第k小的元素，或者说找到排名为k的元素，如果想达到对数级复杂度，关键也在于每个节点得知道他自己排第几。

比如说你让我查找排名为k的元素，当前节点知道自己排名第m，那么我可以比较m和k的大小：

1、如果m == k，显然就是找到了第k个元素，返回当前节点就行了。

2、如果k < m，那说明排名第k的元素在左子树，所以可以去左子树搜索第k个元素。

3、如果k > m，那说明排名第k的元素在右子树，所以可以去右子树搜索第k - m - 1个元素。

这样就可以将时间复杂度降到O(logN)了。

class TreeNode {
    int val;
    // 以该节点为根的树的节点总数
    int size;
    TreeNode left;
    TreeNode right;
}


'''
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(r):
            if r:
                return inorder(r.left) + [r.val] + inorder(r.right)
            else:
                return []

        return inorder(root)[k - 1]



class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 利用 BST 的中序遍历特性
        self.res = 0
        self.rank = 0
        self.traverse(root, k)
        return self.res

    def traverse(self, root: TreeNode, k: int) -> None:
        if root is None:
            return
        self.traverse(root.left, k)
        # 中序遍历代码位置
        self.rank += 1
        if k == self.rank:
            # 找到第 k 小的元素
            self.res = root.val
            return
        self.traverse(root.right, k)
