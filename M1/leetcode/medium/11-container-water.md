a two pointer solution problem,
the pointers used are converging pointers

we are given an integer array,
the array consists of heights of the vertical lines,
our objective is to, find the two lines with the most area,
we return the two lines which forms a container, and holds the most water possible

we use two pointers left and right to come from both sides,
we calculate the area of the container with,

height = min(heights[left], heights[right])
width = right - left
area = height * width

the minimum of two values at the pointer left and right multiplied by right - left, 
the area is essentially a rectangle, length * breadth
the length is obtained by right-left and breadth using the min of two values,
this is so that the container actually encloses on all sides

now we keep track of the max_area through out the array with max(max_area,current_area)
if the height of the two pointers are not equal, we move the smaller pointer inward of the array,

this loop is iterated until left pointer < right pointer fails, that means the array is iterated completely,
now the max_area is returned