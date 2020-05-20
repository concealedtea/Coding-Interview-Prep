from LinkedList import LinkedList

def remove_dups(l1):
    if l1.head is None: return -1
    current = l1.head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return l1

def remove_dups_no_buffer(l1):
    if l1.head is None: return -1
    current = l1.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return l1.head

ll = LinkedList()
ll.generate(10, 0, 9)
print("L1 before: " + str(ll))
remove_dups(ll)
print("L1 after: " + str(ll))

ll.generate(10, 0, 9)
print("L1 before: " + str(ll))
remove_dups_no_buffer(ll)
print("L1 after: " + str(ll))