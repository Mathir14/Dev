Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

intersection of two arrays — just finding common elements between two lists
store one as a set for O(1) lookups

scan through the second, add to result set if it exists in the first
convert result to list before returning

set ensures uniqueness, so no duplicates in output
