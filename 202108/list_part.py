from typing import List, Sized


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return f"Node <{self.val}, {self.next}>"

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        low_h, low_t = None, None
        high_h, high_t = None, None
        
        cur = head
        while cur is not None:
            if cur.val < x:
                if low_h is None:
                    low_h = cur
                    low_t = cur
                else:
                    low_t.next = cur
                    low_t = cur
            
            elif cur.val >= x:
                if high_h is None:
                    high_h = cur
                    high_t = cur
                else:
                    high_t.next = cur
                    high_t = cur
            cur = cur.next
        
        high_t.next = None
        low_t.next = high_h
        
        return low_h



tests = [
    [
        [1,4,3,2,5,2],
        3
    ]
]

for t in tests:
    l = t[0]
    x = t[1]
    head = None
    tail = None
    for i in l:
        n = ListNode(val=i)
        if head is None:
            head = n
            tail = n
        else:
            tail.next = n
            tail = n
    r = Solution().partition(head, x)
    while r is not None:
        print(r)
        r = r.next