# https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None
        oldnew = {}

        curr = head
        while curr:
            oldnew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            clone = oldnew[curr]
            clone.next = oldnew.get(curr.next)
            clone.random = oldnew.get(curr.random)
            curr = curr.next

        return oldnew[head]
