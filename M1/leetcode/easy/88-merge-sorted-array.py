# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            nums1[:n] = nums2[:n]
            return
        replace = m+n-1
        pn1 = m-1
        pn2 = n-1
        while pn2 >= 0 and pn1 >= 0:
            if nums2[pn2] >= nums1[pn1]:
                nums1[replace] = nums2[pn2]
                pn2-=1
            else:
                nums1[replace] = nums1[pn1]
                pn1-=1
            replace-=1
        while pn2>=0:
            nums1[replace]= nums2[pn2]
            replace -=1
            pn2-=1