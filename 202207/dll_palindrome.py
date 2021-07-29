from sympy import N


class Node:
    def __init__(self, v):
        self.data = v
        self.next = None
        self.prev = None


def check_palindrome(head): 
    c = head
    while c.next is not None:
        c = c.next

    tail = c
    palindrome = True
    while head is not None and tail is not None:
        if head == tail:
            break
        if head.data == tail.data:
            head = head.next
            tail = tail.prev
        else:
            palindrome = False
            break

    return palindrome


def create_ll(string, index=0):
    if index >= len(string):
        return None
    else:
        n = Node(string[index])
        n.next = create_ll(string, index+1)
        if n.next is not None:
            n.next.prev = n
        return n


tests = [
    "malayalam",
    "ab"
]

for t in tests:
    head = create_ll(t)
    print(t, check_palindrome(head))



