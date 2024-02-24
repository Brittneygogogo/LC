
'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
https://leetcode.cn/problems/longest-consecutive-sequence/solutions/276931/zui-chang-lian-xu-xu-lie-by-leetcode-solution/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

不要求序列元素在原数组中连续

'''
class Solution:
    def longestConsecutive(self, nums):
        longest_seq = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_seq = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_seq += 1

                longest_seq = max(longest_seq, current_seq)

        return longest_seq

x = Solution()
#0 1 2 3
print(x.longestConsecutive([3,7,2,5,10,6,0,1]))