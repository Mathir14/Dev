# https://leetcode.com/problems/majority-element/

# count method

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) >= (len(nums)/2):
                return i
            
# Boyre - Moore Majority Vote 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lead = nums[0]
        vote = 1
        for i in nums[1:]:
            if vote == 0:
                lead = i
            if i == lead:
                vote +=1
            else:
                vote -=1
        return lead