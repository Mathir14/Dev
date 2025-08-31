# https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(set(nums))
        length = 1
        current = 1

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1] + 1:
                current += 1
                length = length if length > current else current

            else:
                current = 1

        return length
