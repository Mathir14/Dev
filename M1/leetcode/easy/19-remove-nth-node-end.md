Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

we are required to remove the node at n-th position from the end of the linked list,
and return the modified linked list

for the new linked list we create a dummy as the new head,
we have two pointers, slow and fast,

the logic is simple,

consider a given linked list 1 2 3 4 5
let's say we need to remove 2nd node from the end which is 4,

we can move one pointer n times from the start,
lets say we move fast n times which is 2,
so fast is currently at node 2,

now, if we move both fast and slow one node at the same time,
when fast reaches the end, slow will be just before the target node,

fast - 2

move both at once,

fast - 3 slow - 1
fast - 4 slow - 2
fast - 5 slow - 3,

which is just before the target node

and now we can just do
slow.next = slow.next.next so
the node 4 gets overwritten by node 5,

this is the core logic,
we move n times using for loop
were we move fast forward till n by
fast = fast.next

and then we move both slow and fast at once using
slow = slow.next
fast = fast.next in a while loop

and finally we perform
slow.next = slow.next.next
which remvoes the nth node from the end,

and we return dummy.next since dummy itself is a placeholder head
