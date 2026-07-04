class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxWater = 0

        while left < right:
            # Calculate current water
            h = min(heights[left], heights[right])
            w = right - left
            water = h * w
            maxWater = max(maxWater, water)

            # Move the shorter bar inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxWater