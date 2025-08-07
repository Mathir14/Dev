Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0

prefix sum tells us sum of elements from start to current index

if sum of a subarray is divisible by k,
then total_sum % k == 0

for a subarray nums[i+1 to j] to be valid:
prefix[j] - prefix[i] % k == 0 ⇨ prefix[j] % k == prefix[i] % k

so if we’ve seen same mod before,
it means the subarray from i+1 to j has sum divisible by k

we don’t care about actual subarrays,
we just count how many times same mod has appeared

because every previous match gives us one valid subarray ending here

this is why we do:
count += prefix_map[mod]

same logic as equal 0s and 1s:
if balance or mod repeats,
the range between is a net-zero change (either balanced 0s/1s or divisible by k)
