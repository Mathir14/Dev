Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Target is to find the smallest length subarray whose sum is ≥ target.

Constraints say all nums ≥ 1, so window always moves forward. That means:

No point in going beyond target-sized window since you’d already have hit the sum if possible.

But then I realized values can be big, like [1,1,1,1,2,6] for target 6 – here smallest window is just [6] (length 1), not necessarily early.

Sliding window:

Use a left pointer, curr_sum to hold the window sum, and min_len to track smallest valid window.

Expand right, add to curr_sum.

While curr_sum ≥ target:

Update min_len to right - left + 1

Shrink window from left, subtract from curr_sum, move left forward

At the end, return 0 if no window found (min_len untouched), else return min_len.
