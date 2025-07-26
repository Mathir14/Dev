Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

the problem requires us to return the linked list from the middle of it,
used slow/fast pointers - Floyd's Tortoise and Hare

tortoise is the slow pointer,
hare is the fast pointer,

hare is twice as fast compared to tortoise in this problem,
when tortoise moves 1 element,
hare moves 2 elements,

so when hare reaches the end of the linked list,
tortoise is at the middle of it.

same logic is applied in this problem,
we have two pointers slow and fast, both assigned at head.

we move slow one element at a time,
and fast two elements at a time

we iterate this till fast does not have a next meaning fast is at end,
that means fast has iterated through the linked list,
which means slow is at the middle of it.

we return slow once fast is at the end.
