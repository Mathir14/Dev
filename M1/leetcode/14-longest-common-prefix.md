# initial solution

this problem is about finding the longest common prefix, 
it sounds easy to solve but needs thinking,

the problem can be split into two parts,
one is the first string strs[0], then the compare the rest to it

edgecase:
if not strs:
    return ''

reason: 
this returns empty string since there is no common prefix

the apporach i took in my initial solution was to use hash map to store the characters
of the first string in the list of strings strs
and then use count to prevent it from going out of range

for i in strs[1:]:
    if count >= len(i) or i[count] != map[count]:
        return outp

this block of code is the important piece to the puzzle,
since we already have the first string strs[0] in hash map,
we start from strs[1] in the for loop

the if condition is a breaker statement where it returns the current outp if the current index value of
the strings didn't match with the coressponding index value of the key string strs[0]

if the if statement did not execute, it means the value of the current index matches between all strings so the value is added to outp

and once this process has been done for every index using count in while loop
the outp is returned at the end

# after thoughts and optimal solution

the initial solution works fine and achieved a runtime of 1ms when submitted
but the thought of using a seperate loop and a dict for storing a string did not settle with me,
especially when the problem did not require it.

used 2d indexing to,
look up the current index value during the iteration instead of,
storing it permanently in a dict and then look it up at every iteration,
this saves numbers of operations needed and reduces runtime by essesntially retrieving the key string values using it's index instead of a dict.

this led to a runtime of 0ms after submitting.

Some solutions use:
import os
return os.path.commonprefix(strs)

while this works,
it compares character by character,
it hides the actual logic
it’s fine for quick scripts, not for demonstrating skill.
