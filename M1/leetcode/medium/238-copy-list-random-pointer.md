A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:
Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]

So the problem’s about copying a linked list with .next and .random pointers.

At first, I was confused about what Node(curr.val) actually does. Turns out, it just makes a new node with the value copied, but .next and .random are empty for now.

Then I wondered, why do we even need that dictionary? What’s the key and what’s the value?

The keys are the original nodes themselves (not just their values), and the values are the clones of those nodes — but just empty shells at first.

I thought, can’t we just copy .val and .next in one pass, and do .random later? But nope, the .next or .random might point to nodes not created yet, so wiring has to wait.

So in the first pass, we make clone nodes with just .val. In the second pass, we assign .next and .random for each clone by using the dictionary to find clones of the original node’s .next and .random.

When I see clone.next = old_to_new.get(curr.next), what’s going on is: we use curr.next — which is a reference to an original node — to find its clone in the dict, then assign that clone as .next of the current clone. It’s reference matching, not value copying.

I realized the dictionary doesn’t store just values, it stores entire clone node objects. So .get() returns a clone node object (with .val set and .next, .random initially None).

I also thought if we can just create clones on the fly while wiring, but nope — because we need all clones to exist before wiring .next and .random.

Every variable like curr, clone, or .next and .random is basically a pointer to a node in memory. So when we assign clone.next = something, we’re just wiring that pointer to point to the right clone node.

Basically, this whole problem is about passing references around, not copying values — except for copying .val when making the clone.

The dict maps original node references to clone node references, then we use that to rebuild the linked structure with new nodes.

So the whole thing feels like a bookmarking system: first create all the clone “pages” (nodes), then connect those pages with .next and .random links.

It’s tricky because .random makes it more like a graph than a simple list, and you need to manage references carefully.

Took me two hours, but now I get that the magic is in how references work — matching original node references to clone node references, and wiring clones together.

That’s why you can’t do it in one pass — you need to have all clones ready before linking.

In short, nothing but the .val gets copied as a value. Everything else is just references being passed and reassigned.
