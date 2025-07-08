# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# initial thought process
# iterate through each element in the array
# check if the element is already present in the result list/set
# if it is present then it is duplicate
# if it's not then append the element to the result list/set

# after thoughts and the optimal solution
# realized i can simply convert the list to a set and then compare the length of both of them
# an efficient method since the probem doesn't require us to retrieve or display the duplicate element