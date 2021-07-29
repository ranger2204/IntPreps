class Node:
    def __init__(self, k, d):
        self.next = None
        self.prev = None
        self.k = k
        self.d = d


class LRUCache:

    def __init__(self, capacity: int):
        self.max_items = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail
        self.lookup = {}

        
    def remove(self, n):
        p = n.prev
        q = n.next
        p.next = q
        q.prev = p
        
    def add(self, n):
        old = self.head.next
        self.head.next = n
        n.next = old
        old.prev = n
        
    def get(self, key: int) -> int:
        if key in self.lookup:
            n = self.lookup[key]
            self.remove(n)
            self.add(n)
            return n.d
        else:
            return -1


    def put(self, k: int, v: int) -> None:
        n = Node(k, v)
        if len(self.lookup) >= self.max_items:
            r = self.tail.prev
            self.remove(r)
            del self.lookup[r.k]
        self.add(n)
        self.lookup[k] = n


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        
cache = LRUCache(3)
cache.set_data(1, 'a')
cache.set_data(2, 'b')
cache.set_data(3, 'c')
cache.set_data(4, 'd')

cache.print_cache()

cache.get_data(3)
cache.print_cache()
cache.get_data(2)

cache.print_cache()
cache.set_data(5, 'e')


