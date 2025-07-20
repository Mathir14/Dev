#https://leetcode.com/problems/concatenation-of-array/description/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    
# used list multiplication to simply multiply the nums list times 2 and return it,
# time and space complexity of O(n) as we iterate through the array only once and form a list directly using multiplication
