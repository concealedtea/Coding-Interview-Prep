from LinkedList import LinkedList
# Detect if there is a loop
# Find the meeting point
# Find the start of the loop
def findBeginning(ll):
    fast = slow = ll.head
    # Find the starting node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast: break
    if fast == None or fast.next == None: return None
    # Find the start
    slow = ll.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow