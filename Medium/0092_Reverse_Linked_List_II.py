# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head):
        pre, cur, tail = None, head, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre, tail
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return None
        if m >= n: return head
        outsideHead = dummy = ListNode(0)
        windowHead = windowTail = head
        dummy.next = head
        # Set Window Size
        for i in range(n-m):
            windowTail = windowTail.next
        # Adjust till you are at correct starting point
        for i in range(m - 1):
            outsideHead = windowHead
            windowHead = windowHead.next
            windowTail = windowTail.next
        # Isolate and reverse window
        outsideTail, windowTail.next = windowTail.next, None
        reversedHead, reversedTail = self.reverse(windowHead)
        # Combine
        outsideHead.next = reversedHead
        reversedTail.next = outsideTail
        return dummy.next