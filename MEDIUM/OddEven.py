

def findnumber(nums):
    n = len(nums)
    left = 0
    right = n
    mid_odd = (n // 2) % 2
    while left < right:
        mid =  (left + right) // 2
        if nums[mid - 1] == nums[mid] and mid_odd:
            left = mid + 1
        else:
            right = mid -1

    return left



print(findnumber([1,1,5,5,6,6,2,2,4,3,3]))