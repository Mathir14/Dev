Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

a simple linked list problem,
so we set left and right at head for simpler traverse,
we keep moving right until it's val is different from left,

and when they're not equal,
we assign left next as the right,
and we move left to the next,

finally we do
left next = None to avoid any cycle due to leftover
