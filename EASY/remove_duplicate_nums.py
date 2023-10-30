#i 指向不含重复元素序列的最后一个元素
#j 指向未进行决策的序列的首个元素


def removeDuplicates(nums):
    i = 0
    j = 0
    if len(nums) == 0:
        return 0

    for _ in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    print(nums)
    return i + 1

#所有letter都只出现2次
#原地删除重复元素 fast和slow保持2/k的距离

def removeDuplicates2(nums):
    slow = 2
    fast = 2
    if len(nums) < 2:
        return 0

    while fast < len(nums):
        if nums[slow - 2] != nums[fast]:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1
    print(nums)
    return slow + 1




print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


print(removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))

