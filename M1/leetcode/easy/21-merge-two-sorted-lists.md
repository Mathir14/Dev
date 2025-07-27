You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

we are required to merge two sorted linked lists
so we create a new linked list with dummy as head node,

and we use current pointer to do the operations,

given two linked lists,
we iterate through them using while to check if both of them have values

we compare the value of list1 and list2 using .val
and we set the smaller one as the
next node using current.next = smaller node
and we move the smaller node to the next one using .next

now we move current forward to the tail at every iteration so new nodes
can be added

if the while loop fails, it means either of the linked list is empty which could be a result of odd sized linked lists
so we do a final operation where we add the leftover node using

current.next = list1 if list1 else list2
which means if list1 has any leftover node, it gets added,
if it doesn't then list2 gets added,
its None if both are empty which is not an issue

we return dummy.next since dummy is a placeholder head
and .next has the actual values

time O(n+m)
space O(1)
