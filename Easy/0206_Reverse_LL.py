# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        return head