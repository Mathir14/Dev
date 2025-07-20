one of the easiest problems to solve,

we are given an array,
we are required to return the count of every shape of subarray we can make using 0s in that array
such as [0] or [0],[0] or [0][0][0]
much like the count the combination of squares problem from our childhood

instead of counting every combination of sub array, we can simply use this simple trick
store the count in total

[0][0][0]
the count of this is simply 6
why? theres 3 0s
and 2 combination of 0,0s
and 1 0,0,0

instead of doing this we can instead do,
use a variable to keep track of the 0 streak
for each next 0, add the streak with it,

example
for 0 0 0
for first 0, streak = 0, so total = streak + 1 = 1
for second 0, streak = 1, so total += streak + 1 which is 1 + 1 + 1
for third 0, streak = 2, so total += streak + 1 which is 3 + 2 + 1
which is 6, same as the manual sub array method but much faster, simpler and efficient

if the streak breaks meaning a non 0 element is found, the streak simply goes back to 0,
and this process is repeated till the end of the array
and then total is returned

time O(n)
space O(1)
