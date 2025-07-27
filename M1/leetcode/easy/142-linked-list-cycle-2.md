Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

we reuse the floyd's tortoise hare algorithm to meet the point of the cycle first,
two pointers slow and fast

we move slow one node and fast two node at a time,
if there is a cycle, then slow and fast will be equal,

and now at the point of the cycle,
we bring the slow pointer back to head,

and now move both of them one node at a time,
when they're equal again, that is the start of the cycle

dry run:
consider a linked list 1 2 3 4 where 4 cycles to 2
we have slow and fast,
for each itertion

slow and fast head,
slow moves one node to 1, fast moves 2 nodes to 2
slow 2 fast 4

which is the meeting of cycle,
so we bring slow to head
so slow at head

now we move both pointers one node at a time,
so slow at 1 fast at 4
slow at 2 fast at 2 because of cycle,

and now they match, so we return slow which is the start of the cycle

time O(n)
space O(1)
