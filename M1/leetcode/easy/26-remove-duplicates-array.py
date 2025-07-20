# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stayer = 1
        for finder in range(1,len(nums)):
            if nums[finder] > nums[stayer-1]:
                nums[stayer] = nums[finder]
                stayer+=1             
        return stayer