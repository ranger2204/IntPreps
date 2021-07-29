class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def max_profit(root: Node) -> int:
    
    def recur(root, index):
        if root is None:
            return 0
        else:
            
            if index%2 == 0:
                s = max(
                        root.value +recur(root.left, index+1) + recur(root.right, index+1),
                        recur(root.left, index) + recur(root.right, index)
                    )
            else:
                s = recur(root.left, index+1) + recur(root.right, index+1)
                
            return s
        
    return max(recur(root, 0), recur(root, 1))



root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(4)
root.left.right = Node(2)

root.right.right = Node(2)

print(max_profit(root))