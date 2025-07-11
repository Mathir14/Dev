first medium problem I've laid my hands upon

# initial solution - failure

initial thought of a solution was to use nested lists

handled edgecases:

if None in strs:
    return [strs]
this returns an empty nested list

if len(strs) == 1:
    return [strs]
this returns the strs list as a nested list as specified

stored the first element in the result list as the first group

used for i loop to iterate through the rest of the elements from 2nd element

used inner j loop as the iterator to compare the current element from the strs with the
groups in the result list

if they match, it is appened to the element in the j loop 
and breaks to move on to the next element from the outer loop

if the current element matches with none of the groups in the inner j loop
it is then appended to the end of the result list as a new group 

once all the elements are traversed from the outer loop
the result list is returned 

reason of rejection:
while the solution works, it is inefficient due to several factors:
nested loops
every comparison creates a new Counter object which leads to high overhead
this leads to exceeding time limit and rejection of the solution

while it is a solution, it is inefficient and not scalable for large inputs
decided to look for other alternatives instead of nested lists

# sorted tuple method

decided to fall back to using dictionaries

the base of this solution is that,
every anagram when sorted forms the same string
example: "eat", "tea", and "ate" all become "aet" when sorted.

used defaultdict to set an empty list, which can be done by
a normal dict with an extra step of checking if the key is not present and assigning it an empty list manually

used for loop to traverse through strs
used sorted(x) function to obtain the sorted string, 
used tuple instead of list as they're faster to traverse
used the sorted string as the key and added the current string in comparison to it

as the values are stored inside a list per key, used a list() function to covert them into a nested list when returning

this method is much more simple and more efficient compared to using lists for the whole problem,
made me realise not everything needs to be done the hard way.