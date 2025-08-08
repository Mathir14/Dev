Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15

so the problem requires us to, return the count of subarrays whos sum is equal to the goal,

so we keep a prefix running sum which is the sum of all values seen till any point,
and we store the prefix in the hash map at every iteration,

and the way we get the count is,
for any prefix sum, we check if prefix - goal is in the hash map,

if it is, then we += count with that prefix freq

to understand it simpler,
consider each freq value as checkpoints,

for let's say freq of 0 is 5,
then all of those 0s each represent a subarray which can be formed,

and then update the freq of current prefix sum with 1

and we finally return count

time O(n)
space O(n)
