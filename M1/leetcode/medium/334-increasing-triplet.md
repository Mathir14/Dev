we are asked to find increasing triplet, which means
we need to return three values in the array which increase in order, without changing their actual position

assume an array,
10 2 9 4 5
the triplet would be 2 4 5
the element can be present at any index but in order

we have two pointers,
first and second,
we track the smallest element, and assign it as first,
then we find the next element which is greater than first, and assign it as second,
if we find an element greater than both first and second, then that is the third,
we update first or second if the current number is smaller than or equal to them respectively

if all conditions are satisfied, then return True
else False
