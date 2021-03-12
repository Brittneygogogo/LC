import sys
class Solution:
    def threesum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = list()
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] == target:
                    ans.append(nums[first])
                    ans.append(nums[second])
                    ans.append(nums[third])
        return ans

s = Solution()
print(s.threesum([2,5,7,4], 11))


# class Solution:
#     def threeSumClosest(self, nums, target):
#         nums.sort()
#         n = len(nums)
#         best = 10 ** 7
#
#         # 根据差值的绝对值来更新答案
#         def update(cur):
#             nonlocal best
#             if abs(cur - target) < abs(best - target):
#                 best = cur
#
#         # 枚举 a
#         for i in range(n):
#             # 保证和上一次枚举的元素不相等
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             # 使用双指针枚举 b 和 c
#             j, k = i + 1, n - 1
#             while j < k:
#                 s = nums[i] + nums[j] + nums[k]
#                 # 如果和为 target 直接返回答案
#                 if s == target:
#                     return target
#                 update(s)
#                 if s > target:
#                     # 如果和大于 target，移动 c 对应的指针
#                     k0 = k - 1
#                     # 移动到下一个不相等的元素
#                     while j < k0 and nums[k0] == nums[k]:
#                         k0 -= 1
#                     k = k0
#                 else:
#                     # 如果和小于 target，移动 b 对应的指针
#                     j0 = j + 1
#                     # 移动到下一个不相等的元素
#                     while j0 < k and nums[j0] == nums[j]:
#                         j0 += 1
#                     j = j0
#
#         return best

'''
找三数之和和为0。
特殊判断，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
对数组进行排序。
遍历排序后数组：
若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R移到下一位置，寻找新的解
若和大于 0，说明 nums[R] 太大，R 左移
若和小于 0, 说明 nums[L]太小，L 右移

'''
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        res = []
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

x = Solution()
print(x.threeSum([0,1,1,2,3,3]))