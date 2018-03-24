class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        cp = dummy
        while cp.next:
            if cp.next.val == val:
                cp.next = cp.next.next
            else:
                cp = cp.next
        return dummy.next
