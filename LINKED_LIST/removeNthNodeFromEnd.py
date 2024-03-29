'''
删除倒序的第K个节点
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/solutions/450350/shan-chu-lian-biao-de-dao-shu-di-nge-jie-dian-b-61/?envType=study-plan-v2&envId=top-100-liked

让 first 比 second 超前了 n 个节点，当first遍历到链表的末尾， second为倒数第n个节点
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 虚拟头结点
        dummy = ListNode(-1)
        dummy.next = head
        # 删除倒数第 k 个，要先找倒数第 k + 1 个节点
        x = self.findFromEnd(dummy, k + 1)
        # 删掉倒数第 n 个节点
        x.next = x.next.next
        return dummy.next

    # 返回链表的倒数第 k 个节点
    def findFromEnd(self, head: ListNode, k: int) -> ListNode:
        p1 = head
        # p1 先走 k 步
        for i in range(k):
            p1 = p1.next
        p2 = head
        # p1 和 p2 同时走 n - k 步
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
        # p1指向n+1时，p2 现在指向第 n - k 个节点
        return p2
# 详细解析参见：
# https://labuladong.github.io/article/?qno=
