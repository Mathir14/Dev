Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

find first and last position of element in sorted array

we binary search twice
first run finds first occurrence, second run finds last occurrence
keep a variable bound to store the latest index where we see the target

if is_first is true, when we find the target we still move left to see if there’s an earlier one
if is_first is false, when we find the target we still move right to see if there’s a later one

time complexity O(log n) because two binary searches
space complexity O(1) constant space
