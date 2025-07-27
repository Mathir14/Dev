You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

we are given a linked list, we have to reorder the linked list in
such a way that,
its smallest element, biggest element, second smallest element, second biggest element and so on...

to do this, we have to split the linked list in two,
we use floyd's tortoise hare algorithm
where we move slow one node at a time
and fast two nodes at a time

so when fast reaches the end of the linked list,
slow is at the middle,

this allows us to use slow as the
second half of the linked list,

and now we reverse the second half of the linked list using the same 3 pointer technique

prev at None, curr as slow which will be the head of the second half,
we use a temp pointer to hold curr's next node,

and assing prev as curr's next,
essentially swapping values

and now moving both forward using
prev as curr
and curr as the temp pointer which held its actual next node

with this, the second half is reversed,

and now we have to link nodes such that,
its one element from node with 1,2,3...
and one element from node with n,n-1,n-2

we use two pointers for this, first and second
and two temp variables ftemp and stemp to hold the next nodes of both slow and fast,

we link the second node as first.next
and we link the ftemp which holds the original next of first to second.next

and now we move forward first and second using,
first,second = ftemp,stemp
which are the actual next nodes of first and second,

this way the pointers link one node from first and one node from second iteratively till either first or second is exhausted
and now to avoid a potential cycle,
we use first.next = None at the very end of the program,

dry run,
1 2 3 4 5

floyds algorithm,
slow at 1, fast at 2,
slow 2 fast 4
slow 3 fast None,

now slow is at middle,
we reverse the second half using slow as new head for it,
1 2 first half
5 4 3 second half

now we link one node at a time,
1 - 5 - 2 - 4 - 3

and so the linked list is reordered

time O(n)
space O(1)
