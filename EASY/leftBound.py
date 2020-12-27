
'''
左右都闭
'''

def left_bound(nums, target):
    left = 0
    right = len(nums) - 1
    # 搜索区间为 [left, right]
    while (left <= right):
        mid = left + (right - left) // 2
        if (nums[mid] < target):
            # 搜索区间变为 [mid+1, right]
            left = mid + 1
        elif (nums[mid] > target):
            # 搜索区间变为 [left, mid-1]
            right = mid - 1
        elif (nums[mid] == target):
            # 收缩右侧边界
            right = mid - 1

    # 检查出界情况
    if (left >= len(nums) or nums[left] != target):
        return -1
    return left

'''
常见写法， 左闭右开
'''
def left_bound1(nums, target):
    left = 0
    right = len(nums)
    # 搜索区间为 [left, right]
    while (left < right):
        mid = left + (right - left) // 2
        if (nums[mid] < target):
            # 搜索区间变为 [mid+1, right)
            left = mid + 1
        elif (nums[mid] > target):
            # 搜索区间变为 [left, mid)
            right = mid
        elif (nums[mid] == target):
            # 收缩右侧边界
            right = mid

    return left



# print(left_bound([1,2,2,2,3,4], 2))
print(left_bound1([1,2,2,2,3,4], 2))