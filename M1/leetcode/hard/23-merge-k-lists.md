Statement:
You are given an array of k linked-lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Constraints:
k == lists.length

0 <= k <= 10⁴

0 <= lists[i].length <= 500

-10⁴ <= lists[i][j] <= 10⁴

Each linked list is sorted in non-decreasing order.

Example Input:
lists = [
1->4->5,
1->3->4,
2->6
]
Output:
1->1->2->3->4->4->5->6

ok so,
we loop through each list in lists,
and if it's not null, we push it into the heap.

but yk, we can't push just (val, node)
cus when two values are same, Python freaks out trying to compare nodes,

so we add count as the second element,
to make sure every tuple is unique and comparable.

(val, count, node) → boom, clean insert.

then we start building the answer list
using a dummy node like always.

while the heap's not empty:
we pop the smallest node

add it to our answer
move curr

if that node had a next, we push that too
again using the updated count to keep it unique

in the end, all lists are merged,
the min values always got picked first,
and we return dummy.next

Why count matters:
not for logic,

just to keep Python's heap happy
when you got like two 1s or two 5s —

without it, you get a TypeError
so we silently add a count to keep things moving.

Dry run
say we got:

[1 -> 4 -> 5]
[1 -> 3 -> 4]
[2 -> 6]
we push:

(1, 0, node1)

(1, 1, node1)

(2, 2, node2)

heap pops (1, 0, node1), adds to result
push (4, 3, node4)
pop (1, 1, node1), push (3, 4, node3)
pop (2, 2, node2), push (6, 5, node6)
... and so on

at every point, we just follow min value order
no sorting, just heap shuffling
and count makes sure all values are unique in comparison

easy-looking problem,
but this count trick for tie-breaking makes it deeper,
