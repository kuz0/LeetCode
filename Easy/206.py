class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 迭代
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
        # 利用栈结构，将链表内容依次压入栈，再从栈依次弹出即可构造逆序。
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
        # 递归
        if not head or not head.next:
            return head

        p = head.next
        n = self.reverseList2(p)

        head.next = None
        p.next = head
        return n
