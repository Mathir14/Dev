# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head

        while right:
            if left.val == right.val:
                right = right.next
            else:
                left.next = right
                left = left.next
        if left:
            left.next = None
        return head
