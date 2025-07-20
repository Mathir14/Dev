# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for fixed in range(len(nums)-2):
            if nums[fixed] > 0:
                break
            if fixed > 0 and nums[fixed] == nums[fixed-1]:
                continue
            left = fixed+1
            right = len(nums)-1
            while left < right:
                total = nums[fixed]+nums[left]+nums[right]
                if total == 0:
                    answer.append([nums[fixed],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif total > 0:
                    right-=1
                else:
                    left+=1
                                  
        return answer