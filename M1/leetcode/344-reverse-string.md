one of the easiest problem related to two pointers,
this problem involves coverging method where two pointers move closer to each other from
the ends of the array

we are required to reverse the string in-place

we are given a string
we have two pointers left and right
consider this string 'hello'

left starts at string[0] h
right starts at len(string)-1 h

while left is lesser than right
we swap using the logic
left,right = right,left

and then move both left and right inward of the string
(left +=1 for forward and right-=1 for backward)

we use while left is lesser instead of less than or equal to
because the last element simply stays in-place, the extra check is redundant
