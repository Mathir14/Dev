# https://leetcode.com/problems/two-sum

# brute force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
                

# hash map

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, value in enumerate(nums):
            key = target - value
            if key in hmap:
                return hmap[key],i
            hmap[value] = i
