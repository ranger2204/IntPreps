class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check_palindrome(c, h):
    if c is None:
        return True, h
    else:
        v, r = check_palindrome(c.next, h)
        if r is not None:
            v = True if r.data == c.data and v is True else False
            return v, r.next



def create_ll(s, index=0):
    if index >= len(s):
        return None
    else:
        n = Node(data=s[index])
        n.next = create_ll(s, index+1)
        return n


tests = [
    "malayalam",
    "abc"
]

for t in tests:
    h = create_ll(t)
    print(t, check_palindrome(h, h))

