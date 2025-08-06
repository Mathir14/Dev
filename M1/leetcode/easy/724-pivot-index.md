Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

we want an index where sum of left side == sum of right side

total sum of array is fixed

at pivot index, total = left + value + right
so right = total - left - value
check if left == right → 2 \* left + value == total

step by step:
set left_sum = 0

loop over nums

for each index:

check 2 \* left_sum + value == total

if yes, return index

else, add value to left_sum and move on

if loop ends, no pivot found → return -1

time:
one full pass to get total O(n)

one full pass to check pivot O(n)

total time = O(n)
