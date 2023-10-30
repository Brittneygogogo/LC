
# 无序， 先变有序，然后双指针两边找，返回值，


def twoSum(nums: List[int], target: int) -> List[int]:
    # 先对数组排序
    nums.sort()
    # 左右指针
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        sum = nums[lo] + nums[hi]
        # 根据 sum 和 target 的比较，移动左右指针
        if sum < target:
            lo += 1
        elif sum > target:
            hi -= 1
        elif sum == target:
            return [nums[lo], nums[hi]]
    return []



#dict模拟hash表，快，记录下来不用回溯，找到就返回，无法解决有多对的情况。如果有多个相同的值就返回第一个
def twoSums(nums, target) :
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


# 除非初始时左指针和右指针已经位于下标 ii 和 jj，否则一定是左指针先到达下标 ii 的位置或者右指针先到达下标 jj 的位置。
#
# 如果左指针先到达下标 ii 的位置，此时右指针还在下标 jj 的右侧，\text{sum}>\text{target}sum>target，因此一定是右指针左移，左指针不可能移到 ii 的右侧。
#
# 如果右指针先到达下标 jj 的位置，此时左指针还在下标 ii 的左侧，\text{sum}<\text{target}sum<target，因此一定是左指针右移，右指针不可能移到 jj 的左侧。
#
# 由此可见，在整个移动过程中，左指针不可能移到 ii 的右侧，右指针不可能移到 jj 的左侧，因此不会把可能的解过滤掉。由于题目确保有唯一的答案，因此使用双指针一定可以找到答案。


# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#     low, high = 0, len(numbers) - 1
#     while low < high:
#         total = numbers[low] + numbers[high]
#         if total == target:
#             return [low + 1, high + 1]
#         elif total < target:
#             low += 1
#         else:
#             high -= 1
#
#     return [-1, -1]

# print(twoSum([4,0,7,3,2,9], 7))
print(twoSums([4,0,7,3,2,9], 7))