really really really easy problem

first hard difficulty problem ever which i solved faster than the easy ones like 2sum

so basically,
we start from either ends,
we keep track of the peak from either sides,
using left_max and right_max

edge case:
if the length of the list is <= 1 we return 0 since we need minimum of three elements to form a container

now with while left < right since we dont want the walls to overlap,
we check if the current wall is bigger than the peak of its respective side,
left_max for left and right_max for right

we store the bigger wall as the peak
and now storing values,
we check where the left or right wall is smaller,
whichever is smaller, we obtain the water using peak - current dip
which is  total += left or right _max - left or right corresponding to the condition

and we move the smaller pointer inward of the array 
once the while loop ends, we return the total

time complexity O(n)
space complexity O(1)