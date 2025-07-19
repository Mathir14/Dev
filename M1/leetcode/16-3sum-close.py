# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        size = len(nums)-1
        for fixed in range(len(nums)-1):
            
            left = fixed+1
            right = size
            
            while left < right :
                
                curr_sum = nums[fixed]+nums[left]+nums[right]
                
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum
                
                if curr_sum < target :
                    left+=1
                    
                elif curr_sum > target:
                    right -=1
                
                else:
                    return closest
                    
        return closest
