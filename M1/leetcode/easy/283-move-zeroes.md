a two pointer array problem where we have to swap the 0s to the last of the array,
for an array [1,0,2,0,0,4]
the 0s should be moved to the last,
such as [1,2,4,0,0,0]
used a for loop to stay in range of the length of the array
if the i - iter, if the value of i in array is equal to 0, do nothing
if not, then swap the values of i,j such as i,j = j,i
and increment j by 1