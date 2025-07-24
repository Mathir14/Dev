Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

this problem requires us to,
return the k most frequent elements in the given array of intergers

first, used hash to count the frequency of all the elements

next, used maxheap to push the most frequent elements to the top of the heap,

heap = [(-value, key) for key, value in hash.items()]

this line, takes the frequency as value and the actual element as key from hash.items()

so now, the frequency is stored as the key,
heaps are by default minheap

so we use -value to turn this into a maxheap,
for lets say value,
10, to store it as maxheap, we store - value so - 10
s
and since - 10 is really small, it's placed at the front of the min heap,
if we want to use it again we simply use - value again when using it, and this way it is a maxheap

now, with the maxheap formed
we simply for k times as asked in loop,
pop the heap so the 'smallest' element is removed and returned,
at every iteration this oocurs,
and we append the said elements into a list and then return it

time best / average O(n long k) worst O(n log n)
space O(n)
