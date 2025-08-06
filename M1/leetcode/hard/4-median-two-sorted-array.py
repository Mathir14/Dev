# https://leetcode.com/problems/median-of-two-sorted-arrays/description/


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums1 += nums2
        nums1 = sorted(nums1)
        mid = 0 + (len(nums1) - 0) // 2

        if len(nums1) & 1:
            return nums1[mid]
        else:
            return (nums1[mid - 1] + nums1[mid]) / 2
