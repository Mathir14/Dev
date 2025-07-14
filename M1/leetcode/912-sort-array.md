# quick sort

this problem requires us to sort an array with atleast 
time complexity O(n log n)
space complexity as minimal as possible

if the len of the array to sort is 1 or lesser, it's sorted or an empty array,
simply return it

drawbacks of quicksort:
almost sorted array & bad pivots
which can degrade time complexity to O(n^2)

to deal with this, used random func to get random pivots
used list comprehensions for partitioning,
left = values lesser than pivot
right = values greater than pivot
center = values equal to pivot

returns the recursive sort of left + center + right

# merge sort

stable sorting technique unlike quick sort,
guaranteed time complexity of O(n log n)
space complexity of O(n)

if the len of the array to sort is 1 or lesser, it's sorted or an empty array,
simply return it

split phase:
mid = length of arr // 2
uses two lists,
left - elements from 0 to mid
right - elements from mid to -1

partition phase:
calls the partitioning function merge() with left and right

two pointers l and r are initially set to 0

uses a while loop to check if both l and r are are lesser than length of left and right respectively

if left[l] is lesser than or equal to right[r]
then append left[l] and increment l by 1

else append right[r] and increment r by 1

the last element from left or right might not have been appended to the merged list,
uses extend function to extend the leftover elements from left[l:] and right[r:]

returns the merged array