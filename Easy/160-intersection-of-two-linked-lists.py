class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # 如果有一个链表为空，返回NULL；
        # 先遍历链表得到 A、B 的长度，如果最后一个节点不同，返回NULL；
        # 使长的链表先走长度差步，然后一起往后走，直到节点相同，返回。
        if headA is None or headB is None:
            return None

        lenA = 1
        a = headA
        while a.next is not None:
            lenA += 1
            a = a.next
        lenB = 1
        b = headB
        while b.next is not None:
            lenB += 1
            b = b.next
        if a != b:
            return None

        a, b = headA, headB
        if lenA > lenB:
            for i in range(lenA - lenB):
                a = a.next
        else:
            for i in range(lenB - lenA):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a

    def getIntersectionNode1(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # 双指针，当节点到了结尾，跳到另一链表的头
        if headA and headB:
            a, b = headA, headB
            while a != b:
                a = a.next if a else headB
                b = b.next if b else headA
            return a
        else:
            return None
