a sliding window problem,
we are given two strings, one main string and one sub string
we are required to return the index of the first occurance of the sub string within the main string,
this means, the sub string can occur multiple times but only the first occurance index should be returned.

if sub string is not present in the main string, we return -1
if no sub string is even given, we return 0

we use sliding window to solve this problem in the most optimal way,
a sliding window is, the range from one pointer to another, these two pointers move together across the string
like sliding a window,

the reason this method is used is because, the window can be the size of the sub string, so
when we slide that window across the main string, the window should catch the first occurance of the sub string, and we return the head of the window which is the index of the first occurance,

the two pointers, left and right
left is at 0
right is at length of the needle, so the left-right window is the same size as the needle which is the sub string

we use while right is <= length of haystack so the window doesn't slide outside the building (the main string)
if the left:right window catches the subtring, we return left which is head of the window,

if not, we increase left and right by 1, sliding the window to the next sequence of characters

O(n*m) time in worst case, n-main string m-sub string, if the sub string is found at the last comparison
no extra space as we only used string slicing
