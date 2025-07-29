You are given a doubly linked list where in addition to the next and prev pointers, each node may have a child pointer, which may point to a separate doubly linked list.

These child lists can also have one or more child nodes, and so on — meaning the structure is multi-level.

Your task is to flatten the list so that all nodes appear in a single-level doubly linked list. After flattening, the child pointers should all be set to null.

🔸 Constraints:
The number of nodes in the multilevel doubly linked list is in the range [0, 1000].

The values of the nodes are all in the range [1, 10⁵].

🔸 Example:
Input (visual):
1---2---3---4---5---6--NULL
|
7---8---9---10--NULL
|
11--12--NULL
Output (flattened):
1-2-3-7-8-11-12-9-10-4-5-6
All child pointers are now null, and all nodes are connected only through next and prev.

The idea is simple: we do a depth-first traversal of the doubly linked list, and whenever we hit a node with a child, we recursively flatten that child list in-place and splice it between the current node and its next.

Here's how it works:

We start with the head and move node by node.

If a node has no child, we just move to the next.

But if it has a child, that means there's a deeper level.
So we:

Store next of the current node safely since we’ll overwrite it.

Run a dfs on child and flatten that part first.

Once the child is flattened, we connect:

curr.next to child_head

child_head.prev back to curr

If there was a next node (before we went into child),
we link that next to the tail of the child list.

Finally, we null out the child pointer since it's now part of the main list.

This goes recursively till all nested levels are flattened inline.

At each level, the dfs returns the tail node of that flattened portion,
so we know how to stitch things back correctly.

No extra space, no new list — just smart pointer juggling using recursion.

Dry Run

ok so,
first we call the dfs function using dfs head
now when we go inside that function,
curr is node which is head so 1
last is None

so now we use a while loop to iterate till there's nodes using curr,
we store the next of curr in nextnode since we'll overwrite it, so we store 2 there,
now, we check if 1 has child — it doesn’t, so the if condition fails.
and so last is curr, meaning that is the max depth of that said node,
and curr = nextnode so we move forward

now curr is 2
again no child
we store its next using nextnode pointer — so 3 is stored
last is curr, and move to 3

now we store next of 3 — which is None
check if 3 has child — it does

we go into the if block
assign the child head which is 7 — the head of the deeper list
to get the child tail (the last guy in the flattened child list),
we recurse: dfs(7)

now we’re back at the top of the function, with curr = 7, last = None
we store next of 7 → 8
no child, so last = curr
move to 8
store next of 8 → None
no child, last = curr = 8
curr = None → while breaks → return 8 (this is tail of child)

so now, child_tail = 8
we set curr.next = child_head → 3.next = 7
and link backward: child_head.prev = curr → 7.prev = 3
curr.child = None
last = child_tail = 8
curr = nextnode (which was None) → while breaks → return 8

now we're back from that dfs
and 8 is now our curr
store next of 8 → None
check if 8 has child — yes
recurse on 11
same logic → at the end return tail = 12

finally, we return the head after full flattening
because the dfs already linked everything inline — child lists got merged into next/prev chain
