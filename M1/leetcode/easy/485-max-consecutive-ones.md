Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

this uses the same logic as the max subarray of 0s,
for every one encountered, you increment the streak by 1,

and when you encount a value that is not 1,
the streak ends and is reset to 0,
you store the max streak and return it
