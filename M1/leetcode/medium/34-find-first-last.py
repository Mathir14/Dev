# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first):
            low, high, bound = 0, len(nums) - 1, -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] < target or (not is_first and nums[mid] == target):
                    low = mid + 1
                else:
                    high = mid - 1
                if nums[mid] == target:
                    bound = mid
            return bound

        first = find_bound(True)
        if first == -1:
            return [-1, -1]
        return [first, find_bound(False)]
