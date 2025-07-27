# https://leetcode.com/problems/reorder-list/description/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        curr = slow
        while curr:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
        first = head
        second = prev
        while first and second:
            ftemp = first.next
            stemp = second.next
            first.next = second
            second.next = ftemp
            first, second = ftemp, stemp
        if first:
            first.next = None
