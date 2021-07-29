class node:
    def __init__(self, val, links):
        self.val = val
        self.links = links


class Solution:
    def traverse(self, cur):
        if cur is None:
            return 0, 0
        else:
            tc = 1
            splits = 0
            for l in cur.links:
                c, s = self.traverse(l)
                if c%2 == 0:
                    print(cur.val, l.val, 'x')
                    splits += 1
                else:
                    tc += c
                splits += s
            # print(cur.val, tc)
            return tc, splits


root = node(1, [])
l = node(2, [])
r = node(3, [node(4,[node(6, []), node(7, []), node(8, [])]), node(5, [])])
root.links = [l, r]

print(Solution().traverse(root))