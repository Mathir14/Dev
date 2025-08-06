# https://leetcode.com/problems/find-pivot-index/description/


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        left_sum = 0

        for index, value in enumerate(nums):
            if 2 * left_sum + value == total:
                return index

            left_sum += value

        return -1
