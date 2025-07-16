# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        arr = [0] * (right+1)
        count = right
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                arr[count] = nums[right] ** 2
                count -=1
                right-=1
            else:
                arr[count] = nums[left] ** 2
                count -=1
                left+=1
        return arr