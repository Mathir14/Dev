A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

we want any index `i` such that `nums[i] > nums[i-1]` and `nums[i] > nums[i+1]`. at least one peak always exists.

intuition

think of the array like slopes.
if you’re standing at `mid` and see the next element (`mid+1`) is higher, then the peak must be on the right side.
if not, then the peak is on the left side or at `mid`.

code dry run

nums = [1,2,1,3,5,6,4]

low=0, high=6
mid=(0+6)//2=3, nums[3]=3, nums[4]=5
nums[mid] < nums[mid+1] → low=mid+1=4

low=4, high=6
mid=(4+6)//2=5, nums[5]=6, nums[6]=4
nums[mid] < nums[mid+1]? no
→ high=mid=5

low=4, high=5
mid=(4+5)//2=4, nums[4]=5, nums[5]=6
nums[mid] < nums[mid+1] → low=mid+1=5

low=5, high=5 → exit

answer = 5, nums\[5]=6 (a peak).

time complexity: O(log n)
space complexity: O(1)
