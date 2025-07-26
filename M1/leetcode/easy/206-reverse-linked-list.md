Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

the problem requires us to reverse the linked list,
we use three pointers,
same logic as using temp in a normal swap between value,
the only difference is we swap while moving forward in a linked list,

we use prev, curr, next
curr is the current node,
next is the next code,
prev is the previous node,

since current node is head at the start of a linked list,
we have prev as None,

we iterate till curr is None meaning we reached the end of the linked list,

the process is as follows,
we keep the next element of curr stored in next so we don't lose it while swapping,
and now we overwrite the next element of curr with prev,
now we move forward by setting
prev as curr
and curr as next

this allows us to swap,
and then move forward the linked list.

once we reach the end, we simply return prev as that is the new head

time O(n)
space O(1)
