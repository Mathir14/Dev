Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Example 3:
Input: nums = [0,1,1,1,1,1,0,0,0]
Output: 6
Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

given binary array, find longest subarray with equal 0s and 1s

idea is to convert 0s to -1s and track prefix sum (running balance), if at any two indices the balance is same, the subarray between them has equal 0s and 1s

store first occurrence of each balance in a hashmap (balance -> index)

loop through array, update balance += 1 if num==1 else -1

if balance seen before, update max_len = max(max_len, i - index_stored)

else store balance with current index

init map with balance 0 at index -1 to handle edge case

return max_len at end

can be modified to count subarrays with equal 0s and 1s by storing count of each balance instead of index, and doing count += balance_map[balance] every time we see the same balance

both run in O(n) time and space
