the problem requires us to,
find the largest sequence, ex

1,2,3,4,5,6,
10,11,12,13,14,15
etc

from the given array of integers

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

first we convert the array into set to avoid duplicate values since we're only looking for consecutive sequence,

we loop through each character, lets say using i
if the value i-1 is not present in the set it means, i is the beginning of the sequence,
so streak is set to 1,

and now we check using while loop, for every value i+1 we can find,
we keep increasing streak by 1 for every consecutive find,

and we use length to keep track of the maximum streak discovered.
