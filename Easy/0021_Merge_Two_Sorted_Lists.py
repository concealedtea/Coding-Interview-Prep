"""
STATEMENT
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

CLARIFICATIONS
- Merges the two lists in increasing order
- If there are two of the same number, we don't care which one goes first
- Returns a singular unique new list
- Assume both lists are already sorted


EXAMPLE
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

COMMENTS
Initial approach is to iterate the lists starting at the first node, comparing values to see if greater than, then adding to new list
Should be O(N+M) time complexity where N & M are the number of elements in each list, this will also have O(1) space complexity as we aren't creating any additional space
Recursion is ineffective here because it would take up unnecessary space during production
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            if not l1 and not l2:
                return None
            return l1 or l2
        dummy = cur = ListNode(0) # Generate dummy and cursor that point to an empty Linked List
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

        