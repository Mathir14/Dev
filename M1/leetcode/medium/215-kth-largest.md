Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Sorted approach

Sort the array in descending order.

Pick the (k-1)th element.

Time: O(n log n) due to sorting.

Space: O(1) (ignoring sort’s internal usage).

Heap approach

Maintain a min-heap of size k.

Push each number, pop if heap grows beyond k.

At the end, heap root is the k-th largest.

Time: O(n log k), better for large n with small k.

Space: O(k) for the heap.
