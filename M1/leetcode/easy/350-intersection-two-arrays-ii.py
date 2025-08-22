# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        n1 = 0
        n2 = 0

        result = []
        while n1 < len(nums1) and n2 < len(nums2):

            if nums1[n1] == nums2[n2]:
                result.append(nums1[n1])
                n1 += 1
                n2 += 1

            elif nums1[n1] < nums2[n2]:
                n1 += 1

            else:
                n2 += 1

        return result
