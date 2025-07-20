simple problem which can be explained in a few step
we are given an array, we are asked to shift it k times
so 1 2 3 for k = 2 is
3 1 2
2 3 1

to reduce dry code, we use a function which takes the array,
start value and end value
and reverses the value of the array within the start and end bounds

we used k %= size of array because,
only the remainder matters as everything else is just repeated shifts,

so instead of shifting some k = 1000,
we can simply shift the remainder of k % n

in first function call, we reverse the entire array, for k = 2
so 1 2 3 4 looks like 4 3 2 1
then in second function call, we reverse elements that are within k,
so index 0 and 1
the reverse looks like this
3 4 2 1
now we reverse the other elements from k to end
it looks like this
3 4 1 2

now doing it manually, 
1 2 3 4 k = 2
4 1 2 3 k = 1
3 4 1 2 k = 0

we reverse the array by swapping the start and end element
and then moving them both inward

in place with O(1) complexity
time complexity of O(n) since any number of n such as 1n 2n 3n is still n
