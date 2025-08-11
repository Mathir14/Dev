You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1

we are given a range, 1 to n,
and we are requied to find the earliest point where a value within n becomes bad,
if a value is bad, everything else that follows is also bad,

first we use two pointers,
left and right, starting at two ends,

we use mid to find the bad value,

if a value is bad,
then we skip the rest of the right-side range,

and move high to the mid value so the current lower bound is low to mid(high)

if a value is not bad,
then we skip the rest of the left-side range,

and move low to mid+1 so the current lower bound is low(mid+1) to high,

this way, when the loop left < right ends,
left will hold the earliest bad value

time O(log n)
space O(1)
