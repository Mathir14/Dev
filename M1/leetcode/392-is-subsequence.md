another two pointer problem,
the pointer requires us to find, if the smaller substring can be formed from the main string,

we have two pointers left and right,
left to iterate the smaller sub string
right for the bigger main string

edge case:
we return True if the sub string to be formed is empty which means it is True

we start with while right < len(bigger string)
because we want right to traverse through the full main string,
we compare the char at left in smaller string and char at right in bigger string,
if they match, we move both by 1
if they dont match only right gets moved by 1,

we return True if left is equal to len of smaller string meaning it has traversed through the entire smaller string
which means it can be formed from the main string,

if the while loop ends, that means the smaller string cannot be formed and so we return False