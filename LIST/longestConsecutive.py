
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 转化成哈希集合，方便快速查找是否存在某个元素
        set_num = set(nums)

        res = 0

        for num in set_num:
            if num - 1 in set_num:
                # num 不是连续子序列的第一个，跳过
                continue
            # num 是连续子序列的第一个，开始向上计算连续子序列的长度
            cur_num = num
            cur_len = 1

            while cur_num + 1 in set_num:
                cur_num += 1
                cur_len += 1
            # 更新最长连续序列的长度
            res = max(res, cur_len)

        return res