from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def reversePrint2(self, head: ListNode) -> List[int]:
#     # 用「分解问题」的思路写递归解法
#     def sub_problem(head):
#         if not head:
#             return []
#         sub_res = sub_problem(head.next)
#         sub_res.append(head.val)
#         return sub_res
#
#     return sub_problem(head)



class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if head:
            return self.reversePrint(head.next) + [head.val]
        else:
            return []
