'''
快慢指针
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        slow, fast = 0, 0
        while (fast < len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1

x = Solution()
print(x.removeDuplicates([1,1,1,2,2,3]))