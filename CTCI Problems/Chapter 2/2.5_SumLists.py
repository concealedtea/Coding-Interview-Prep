from LinkedList import LinkedList
def sumListsBackwards(l1,l2):
    a, b = l1.head, l2.head
    ll = LinkedList()
    carry = 0
    while a or b:
        result = carry
        if a:
            result += a.value
            a = a.next
        if b:
            result += b.value
            b = b.next
        ll.add(result % 10)
        carry = result // 10
    if carry:
        ll.add(carry)
    return ll

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sumListsBackwards(ll_a, ll_b))