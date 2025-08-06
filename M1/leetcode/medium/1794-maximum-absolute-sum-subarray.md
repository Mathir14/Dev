You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

# prefix method

prefix tracks sum from start up to current index.

max_val and min_val track the highest and lowest prefix seen so far.

at each step, the largest abs subarray ending here is abs(prefix – max_val) or abs(prefix – min_val).

update res with those possibilities.

then update max_val or min_val with current prefix if needed.

step by step:
initialize prefix = max_val = min_val = res = 0.

loop num in nums:

add num to prefix.

compare abs(prefix – max_val) and abs(prefix – min_val) with res.

update max_val if prefix is bigger.

update min_val if prefix is smaller.

at end return res.

time & space:
one pass → O(n)

constant extra space

# kadane's method

it's two Kadane runs in one loop.

curr_max keeps the max subarray sum ending here.

max_val is global max subarray sum seen.

curr_min keeps the min subarray sum (most negative) ending here.

min_val is global min subarray sum seen.

the absolute max is max of abs(max_val) and abs(min_val).

step by step:
initialize four vars to 0.

loop through nums:

update curr_max as best of num or continuing the previous sum.

update global max_val.

update curr_min similarly, tracking negative running sums.

update global min_val.

result is max of absolute values of those two.
