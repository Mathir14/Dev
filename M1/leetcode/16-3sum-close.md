similar to 3sum problem,

we are required to return the triplet which is, closest to the target value
not equal, but closest

and there is exactly one triplet which is the correct solution

we are given an unsorted array so we sort using .sort() to iterate through it

we use closest variable to keep track of the sum which is closest to the target value

we use three pointers just like in 3sum
one is fixed, which is used as the stayer pointer
left and right, where left starts at the element next to fixed,
right at the end of the array

we use while left < right since we don't want them to overlap
this problem approach is the same as 3sum but we instead keep track of the sum closest to the target value
initially we assign closest as the first 3 elements

current sum is the sum of current fixed and left and right
we compare closest and current sum as,
absolute of target - current sum and absolute of target - closest till now,
whichever has the least difference to target is the one closest to it

now with updated closest,
we check if current sum is smaller than target, if it is
we move left +=1
if it is larget, we move right -=1
on the curveball that current sum is actually equal to target, 
we return closest on the last else condition

and we have the final return closest outside the main loop which means the array has been traversed,
and the closest value is returned