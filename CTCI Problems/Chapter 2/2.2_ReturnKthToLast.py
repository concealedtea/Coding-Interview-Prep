from LinkedList import LinkedList

def return_kth_to_last(l1, k):
    current = runner = l1.head
    for i in range(k):
        runner = runner.next
    while runner.next:
        current = current.next
        runner = runner.next
    return current

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(return_kth_to_last(ll, 3))