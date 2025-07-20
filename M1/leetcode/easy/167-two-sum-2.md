another two pointer based and sequel to the legendary two sum I problem

how this differs from two sum I:
the original two sum I let us use extra data structure like hashmap since the given array was unsorted,
the sequel two sum II, gives us sorted array and expects us to do it in constant space

it has only one guaranteed solution and we may not use the same element twice

when we find the pair of values whose sum matches the target value, we return their index as [index i+1, index j+1]

this problem uses converging pointers left and right
left, starts at the beginning - 0
and right at the end of the array, len(arr)-1

since we cannot use the same element twice, we cannot let left and right overlap,
so we use while left < right and not <=

we get the sum of values at index left and right,
we use if condition to check if it matches with target value
if it matches, we return [left+1,right+1]
if it doesn't, we move to the next condition,

if val > target:
which means, the sum of values of index left and right is greater than the target value,
so we move right inwards in the array, since the array is sorted,
the values are smaller as we progress from the end to inwards of the array

finally the last condition
if val < target:
which means, the sum of values of index left and right is lesserr than the target value,
so we move left inwards in the array, since the array is sorted,
the values are larger as we progress from the start to inwards of the array

the conditions val > target and val < target allows us to move the required pointer
in the valid direction which lets us match the correct two values and return the indices

this is O(1) space since we iterated through the array only once
and O(n) time since we compare each element in the array