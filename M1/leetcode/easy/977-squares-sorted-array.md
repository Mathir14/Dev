anothe two pointer problem 
this problem involves the converging method,

we are given an sorted integer array, with elements ranging from negative to positive
this problem is not in place so we are allowed to use another data structure to hold values

it requires us, to return a sorted array with the square of the elements,

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

so we begin with two pointers, left and right
left begins at the start which is 0
and right begins at the end of the given array which is len(array)-1

the array arr is the structure we are going to use to store the values,
since we need to store the elements from the end of the list, 
we use count variable which moves inwards negative index from -1 every time a value is stored in arr 

we use a while loop where left <= right to keep the pointers from over-passing
we check if the absolute number of the value at index left is lesser than or equal to the absolute number of the value at index right
if condition is true, we store the square of the value at index right 
and then we move count inward by 1 
and move right inward by 1

if the condition fails,
we stored the element at index left inside arr using count as the index,
then we move count inward by 1 so it points to the next negative index position inwards the array arr,
and move left upwards to the next element inwards to the array

once the loop completes we return the complete array arr