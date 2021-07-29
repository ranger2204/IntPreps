class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def find_bottom_view(root: Node) -> list:
    
    hr_dist = {}
    
    def dfs(root, d):
        nonlocal hr_dist
        if root is not None:
            hr_dist[d] = root
            dfs(root.left, d-1)
            dfs(root.right, d+1)
    

    dfs(root, 0)
    min_hr_dist = min(hr_dist.keys())
    if min_hr_dist < 0:
        min_hr_dist = -1 * min_hr_dist
    view = [0 for i in hr_dist]
    for n in hr_dist:
        view[n+min_hr_dist] = hr_dist[n].data
    print(view)


r = Node(0)
r.left = Node(1)
r.right = Node(2)
r.left.left = Node(3)
r.left.right = Node(4)

find_bottom_view(r)

