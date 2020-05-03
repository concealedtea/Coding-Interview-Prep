# Uses a divide and conquer method similar to binary sort, this lowers the time complexity to 
# only O(N * Log K) where N is the total # of nodes in all lists and K is the number of lists
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l,r)
    
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