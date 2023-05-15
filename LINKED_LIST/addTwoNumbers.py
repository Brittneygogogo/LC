# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 在两条链表上的指针
        p1, p2 = l1, l2
        # 虚拟头结点（构建新链表时的常用技巧）
        dummy = ListNode(-1)
        # 指针 p 负责构建新链表
        p = dummy
        # 记录进位
        carry = 0
        # 开始执行加法，两条链表走完且没有进位时才能结束循环
        while p1 or p2 or carry:
            # 先加上上次的进位
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry, val = divmod(val, 10)
            # 构建新节点
            p.next = ListNode(val)
            p = p.next
        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next
    #