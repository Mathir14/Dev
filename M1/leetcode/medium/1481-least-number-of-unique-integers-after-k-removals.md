Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

Count frequencies of each integer using Counter.

Sort these frequencies in descending order (so smallest counts are at the end).

While k > 0:

Check the smallest frequency (last element).

If it can be fully removed (≤ k), subtract it from k and pop it from the list.

Otherwise, stop.

Answer is the number of remaining frequencies = number of unique integers left.

Time: O(n log n) → for counting and sorting.

Space: O(n) → to store counts.
