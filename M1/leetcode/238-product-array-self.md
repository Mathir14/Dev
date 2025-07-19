a simple problem where i struggled,

the problem requires us to return the product of all elements except i at i index,
so for example

for an array 1 2 2 3
the result should be

for 1s position 2 x 2 x 3 so 12
for 2s position 1 x 2 x 3 so 6
for 2s position 1 x 2 x 3 so 6
for 3s position 1 x 2 x 2 so 4

the result should be
12 6 6 4,
which is the product of every element except the one at the corresponding index,

to get this in code, and in O(n) time, we need minimal overhead
we will use two running values,
prefix and suffix

prefix will hold the product of elements before i
and suffix will hold the product of elements after i

they will *= with every element they come across and keep the value active,
answer[i] *= is used to store that prefix or suffix value in that i position,
every value is initialized as 1 since we cannot use 0 for products

this runs in O(n) time since we go through each element only once
and O(1) extra space since output is generally ignored