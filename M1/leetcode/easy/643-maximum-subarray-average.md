You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

a simple problem, where most people would first opt to use the brute force method, including me,
the brute force method includes,
getting the sum of every element in the current window,
and repeating this completely new again when the window moves an element,

this is unnecessary because,
for example, say an array
1 2 3 4 5 6 7 8 9 10
with window of 3 elements,

what they do is,
1 2 3 - sum 6
2 3 4 - sum 9
3 4 5 - sum 12

this is wasting the already stored and usable values and instead starting over again every single time,

the better method is to,
say 1 2 3 - sum 6
2 3 + 4 -1 - , instead of doing it again, u just add the 4 and remove 1 from the previous result,
so previous sum is 6, add the current 4, and remove the first of previous window,
so 6 + 4 - 1 so 9
same value as the previous method except more efficient since we only calculate one more value per window iteration instead of the whole window again,

the initial
window = sum(nums[:k])

is to store the first k elements so we can 1 next from there,

this is why we use,
for i in range(k, len(nums)):
window += nums[i] - nums[i - k]

that is essentially, adding the current new element
and then subtracting the first element of previous window since the window has been moved one next

then we return the max average by storing the largest sum and then returning it /k
