class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def get_largest_sub_BST(root):
    max_size_so_far = 0

    def recur(root):
        nonlocal max_size_so_far
        if root is None:
            return None, None, 0, True
        else:
            lmx, lmin, lsz, lc = recur(root.left)
            rmx, rmin, rsz, rc = recur(root.right)
            sz = lsz+rsz+1

            if lmx is not None and rmin is not None:
                if lmx <= root.key and rmin > root.key and lc and rc:
                    max_size_so_far = max(sz, max_size_so_far)
                    return rmx, lmin, sz, True
                else:
                    return rmx, lmin, sz, False
            else:
                if lmx is not None:
                    if lmx <= root.key and lc and rc:
                        max_size_so_far = max(sz, max_size_so_far)
                        return lmx, lmin, sz, True
                    else:
                        return lmx, lmin, sz, False
                elif rmin is not None:
                    if rmin > root.key and lc and rc:
                        max_size_so_far = max(sz, max_size_so_far)
                        return root.key, rmin, sz, True
                    else:
                        return root.key, rmin, sz, False

                else:
                    max_size_so_far = max(sz, max_size_so_far)
                    return root.key, root.key, sz, True

    recur(root)
    return max_size_so_far

root = Node(10)
root.left = Node(5)
root.left.left = Node(1)
root.left.right = Node(8)
root.right = Node(15)
root.right.right = Node(7)

print(get_largest_sub_BST(root))