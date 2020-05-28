from LinkedList import LinkedList
def find_intersection(l1,l2):
    shorter = l1 if len(l1) < len(l2) else l2
    longer = l1 if len(l1) > len(l2) else l2
    if l1.tail != l2.tail: return None
    sizeDiff = len(longer) - len(shorter)
    longerNode, shorterNode = longer.head, shorter.head
    for i in range(sizeDiff):
        longerNode.next
    # Is - Identity Check
    # != - Value Check
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    return longer