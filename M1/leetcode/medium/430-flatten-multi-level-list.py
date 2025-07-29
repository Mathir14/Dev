# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


class Solution:
    def flatten(self, head: "Optional[Node]") -> "Optional[Node]":
        def dfs(node):
            curr = node
            last = node  # The last node of the flattened list

            while curr:
                next_node = curr.next
                if curr.child:
                    # Flatten the child list
                    child_head = curr.child
                    child_tail = dfs(child_head)

                    # Connect current node to child
                    curr.next = child_head
                    child_head.prev = curr

                    # If there was a next node, connect it to the child tail
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail

                    curr.child = None
                    last = child_tail
                else:
                    last = curr
                curr = next_node

            return last

        dfs(head)
        return head
