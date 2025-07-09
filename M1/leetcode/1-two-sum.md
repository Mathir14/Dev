brute force :
use nested loops to brute force through the array
use iter 1 to compare every possible value with iter 1 in the array
iter 1 starts from 0 to len-1
and iter 2 from iter1 + 1 to len
this allows for iter2 to start and always be one element ahead of iter1 instead of starting at the same position
the inner loop compares every other element with iter1 element, if the condition (i + j == target) isnt satisfied
it exits the inner loop and the iter1 moves on to the next element, this process is repeated until the iterables are out of elements
or a match is found, if so, it returns the index of i and j as the sum pair that is equal to the target

time complexity O(n^2)

hash map :
in a dict/ hash map, the value is stored as key and the index is stored as value
we use enumerate function to obtain both the index and value of an element in an array

ex :
arr = [1,2,3]
for i, val in enumerate(arr)

using this function, the value of the element is stored in val and it's index is also simultaneously stored in i
we have the value and the target, so we subtract the value from the target to get the required number which is the 2nd value we need
we check if the 2nd value or called complement is present in the hash map,
if it is, it means we found the complement, so we simply return the index of that complement and i which is the index of current value,
if it isn't then we create a new item where the current value is the key and it's index i is stored as the corresponding value

time complexity O(n)

this method is much more optimized as we do not have to iterate through loops comparing every element
look-ups in dict is always constant O(n) so it is significantly better compared to using bruteforce technique
