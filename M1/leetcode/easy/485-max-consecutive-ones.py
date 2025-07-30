# https://leetcode.com/problems/max-consecutive-ones/description/


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev = 0
        streak = 0
        for i in nums:
            if i == 1:
                prev += 1
                streak = streak if streak > prev else prev
            else:
                prev = 0
        return streak
