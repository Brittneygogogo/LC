'''双指针'''
class Solution:
    def trap(self, height) -> int:
        left=0
        right=len(height)-1
        left_max=right_max=0
        ans=0
        while left<=right:
            if left_max<right_max:
                ans+=max(0,left_max-height[left])
                left_max=max(left_max,height[left])
                left+=1
            else:
                ans+=max(0,right_max-height[right])
                right_max=max(right_max,height[right])
                right-=1
        return ans