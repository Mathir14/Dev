# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}
        for idx, value in enumerate(nums):
            if value in hash and abs(idx - hash[value]) <= k:
                return True
            hash[value] = idx
        return False
