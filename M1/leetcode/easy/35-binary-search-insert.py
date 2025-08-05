# https://leetcode.com/problems/search-insert-position/


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(target, low, high):

            if low > high:
                return low

            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return binary_search(target, mid + 1, high)

            else:
                return binary_search(target, low, mid - 1)

        return binary_search(target, 0, len(nums) - 1)
