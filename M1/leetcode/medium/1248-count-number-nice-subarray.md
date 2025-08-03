Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

same logic reused but this time problem asks for subarrays with exactly k odd numbers

no need for a frequency map here, just count odds

whenever you hit an odd number, use up 1 k

if you go over (k < 0), slide left pointer and regain the k only if you move past an odd number

keep adding right - left + 1 to res when valid

again, use atmost(k) - atmost(k-1)

what i learned:

how to reduce new problems into familiar patterns (treat odds like distinct elements)

condition in while loop isn't always about window length, it's about resource limits (here, k used up)

anded everything into pure logic: add right, shrink left, update count only if condition broken
