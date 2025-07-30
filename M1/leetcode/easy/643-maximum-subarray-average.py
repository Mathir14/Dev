# https://leetcode.com/problems/maximum-average-subarray-i/description/


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        max_average = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            max_average = window if window > max_average else max_average
        return max_average / k
