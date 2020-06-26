# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Use Divide and Conquer technique to split work up recursively
        # Runtime O(nlogn), can run in constant space O(1)
        if not lists: return
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val <= r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        if not l: cur.next = r
        else: cur.next = l
        return dummy.next
        