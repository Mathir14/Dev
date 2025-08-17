Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [1,3,5]
Output: 1

Example 2:
Input: nums = [2,2,2,0,1]
Output: 0

array is sorted and rotated, may contain duplicates. goal = find min.
binary search with tweaks for duplicates:

if nums[mid] > nums[high] → min is in right half → low = mid+1

elif nums[mid] < nums[high] → min is in left half or at mid → high = mid

else nums[mid] == nums[high] → duplicates, can’t decide → safely reduce high -= 1
loop ends when low = high → nums[low] is minimum.

dry run
nums=[2,2,2,0,1]

low=0, high=4
mid=2 → nums[2]=2 == nums[4]=1? no → nums[mid]>nums[high] → low=3
low=3, high=4
mid=3 → nums[3]=0 < nums[4]=1 → high=3
low=3, high=3 → stop

nums[3]=0 → min=0

duplicates force the high -= 1 step, which may reduce binary search efficiency, but keeps correctness.
