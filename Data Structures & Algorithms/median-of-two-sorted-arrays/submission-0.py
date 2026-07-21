class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array for O(log(min(m,n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        lo, hi = 0, m
        while True:
            i = (lo + hi) // 2       # partition index in nums1
            j = half - i             # partition index in nums2

            # Values just left/right of the partition (use inf for out-of-bounds)
            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')
            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                # Correct partition found
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return min(right1, right2)
            elif left1 > right2:
                hi = i - 1   # partition in nums1 too far right, move left
            else:
                lo = i + 1   # partition in nums1 too far left, move right