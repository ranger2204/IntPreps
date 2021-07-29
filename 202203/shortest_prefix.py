class Node:
    def __init__(self, val, links={}, end_node=False, frequency=0):
        self.val = val
        self.links = links
        self.end_node = end_node
        self.frequency = frequency


class CustomTrie:
    def __init__(self):
        self.root = Node("-", {}, False, 0)

    def add_string(self, new_str):
        cur_node = self.root
        for c in new_str:
            if c not in cur_node.links:
                cur_node.links[c] = Node(c, {}, False, 0)
            cur_node = cur_node.links[c]
            cur_node.frequency += 1
            # print(cur_node)
        
        cur_node.end_node = True

    def level_traverse(self):
        q = [self.root]
        k = 5
        # while len(q) > 0:
        while k > 0:
            m = len(q)
            while m > 0:
                n = q.pop(0)
                print(f'{n.val}({n.frequency})', end=" ")
                m -= 1
                for l in n.links:
                    q.append(n.links[l])
            print("")
            k -= 1

    def print_least_freq(self):
        result = []

        def recur(cur, accu):
            nonlocal result
            if cur.frequency == 1:
                result.append(accu+cur.val)
                return

            for l in cur.links:
                recur(cur.links[l], accu+cur.val)
        
        recur(self.root, "")
        return result

tests = [
    'dog', 'cat',
     'apricot', 'apple', 'fish'
]

t = CustomTrie()
for s in tests:
    t.add_string(s)

print(t.print_least_freq())