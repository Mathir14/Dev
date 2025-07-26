Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

this problem requires us to return True if the linked list forms a cycle-
meaning a node is pointing to another node before it, forming a cycle.

this problem uses the same principle,
Floyd'a tortoise hare algorithm,

we have two pointers,
slow and fast, on the same principle,

slow moves one element at a time,
fast moves two element at a time,

we iterate through the linked list,
if fast catches up to slow,
meaning fast cycled back to the same element of slow in any iteration,
it means a cycle exists and now slow and fast are at the same element,

and when a cycle is captured, we return True,
if slow and fast does not meet, it means, no cycle exists and so
we return false

time O(n)
space O(1)
