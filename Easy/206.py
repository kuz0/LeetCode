class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        while head:
            post = head.next
            head.next = pre
            pre = head
            head = post
        return pre

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        lst = []
        while p:
            lst.append(p.val)
            p = p.next
        p = head
        while lst:
            p.val = lst.pop()
            p = p.next
        return head

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        p = head.next
        n = self.reverseList(p)

        head.next = None
        p.next = head
        return n
