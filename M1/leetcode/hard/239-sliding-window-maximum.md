You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position Max

---

[1 3 -1] -3 5 3 6 7 3
1 [3 -1 -3] 5 3 6 7 3
1 3 [-1 -3 5] 3 6 7 5
1 3 -1 [-3 5 3] 6 7 5
1 3 -1 -3 [5 3 6] 7 6
1 3 -1 -3 5 [3 6 7] 7
Example 2:

Input: nums = [1], k = 1
Output: [1]

sliding window maximum – intuition and logic

problem:
given an array and window size k, find the maximum in each sliding window of size k

first thought:
heap can do it but it's messy. removing outdated elements isn't cheap. we want O(n). so we use a deque (double-ended queue)

why deque:
deque stores indices of useful elements in decreasing order of value.
front of the deque always holds the index of the current window's max
any number smaller than current number gets removed from the back – they're useless now

logic step by step:
for each index i in array:

1. remove from back while current number is greater than deque's last index value
2. append i to deque
3. if deque front is out of current window (i - k), remove it from front
4. if i >= k - 1, we've hit a valid window, so add nums\[deque\[0]] to result

why i - k:
because window is from i - k + 1 to i. anything at i - k or before is outside

intuition:
you filter out non-max elements behind the scenes
you always keep the current window’s max at front
you only keep useful values, rest get thrown out when a bigger one shows up or they fall outside the window
