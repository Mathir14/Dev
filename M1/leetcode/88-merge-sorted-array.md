an in place two pointer problem,
we are given two sorted arrays

the problem requires us to merge these two arrays into the bigger array,
the bigger array has 0 elements corresponding to the number of elements in the smaller array

two edgecases,
if n is 0 that means there is no element from smaller array which needs to be merged into bigger array so we return nothing
if m is 0 that means there is only 0s in bigger array, we simply stored ever element in smaller array to insde the bigger array

we start from the end of smaller array
and from the end of actual values inside the bigger array except the 0s at the end

we compare both element from the pointers pn1 and pn2, we place the bigger value at the end of the array
using replace which shrinks by 1 after every placement

we move the pointer which held the bigger value inward to its array

and then we add the leftover elements from the smaller array into the bigger array using replace 