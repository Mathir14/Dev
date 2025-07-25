# https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        val = set(nums)
        length = 0

        for i in val:
            if i - 1 not in val:
                count = i
                streak = 1

                while count + 1 in val:
                    count += 1
                    streak += 1

                length = length if length > streak else streak

        return length
