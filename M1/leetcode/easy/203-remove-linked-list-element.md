Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

remove linked list elements — need a dummy node to handle head deletions cleanly
dummy points to head, we walk with `curr`, always checking `curr.next`

if value matches, skip the node by rerouting `curr.next`
else just move forward

return `dummy.next` at the end to skip any deleted head
no edge case mess, simple and clean fix
