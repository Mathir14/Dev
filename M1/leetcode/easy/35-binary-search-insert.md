Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

search insert position — binary search, recursive
base case: if low > high, target isn't found, return low as insert pos

mid = average of low and high
if target found at mid, return mid

if target > mid, search right half
if target < mid, search left half

simple, clean, no extra checks needed
recursive stack used but logic is straightforward
works for both found and not-found cases
