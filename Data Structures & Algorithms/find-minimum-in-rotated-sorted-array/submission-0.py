class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum must be to the right of mid
            if nums[mid] > nums[right]:
                left = mid + 1
            # Otherwise, the minimum is at mid or to its left
            else:
                right = mid
        
        return nums[left]