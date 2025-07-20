# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height)-1
        total = 0
        left_max = 0
        right_max = 0

        if len(height) <= 1:
            return 0

        while left < right:
            if height[left] > left_max:
                left_max = height[left]

            if height[right] > right_max:
                right_max = height[right]

            if height[left] < height[right]:
                total += (left_max - height[left])
                left +=1
            else:
                total += (right_max - height[right])
                right -=1

        return total