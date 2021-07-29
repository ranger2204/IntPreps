class newNode:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        

def get_inorder(root):
    if root is None:
        return "<e>"
    else:
        res = get_inorder(root.left)
        res += root.key
        res += get_inorder(root.right)
        return res
        
def get_preorder(root):
    if root is None:
        return "<e>"
    else:
        res = root.key
        res += get_preorder(root.left)
        res += get_preorder(root.right)
        return res
        
def check_is_subtree(s, t):
    in_s = get_inorder(s)
    in_t = get_inorder(t)
    
    if in_s not in in_t:
        return False
        
    pre_s = get_preorder(s)
    pre_t = get_preorder(t)
    if pre_s not in pre_t:
        return False
    return True
    
    
    
T = newNode('a')
T.left = newNode('b')
T.right = newNode('d')
T.left.left = newNode('c')
T.right.right = newNode('e')
 
S = newNode('a')
S.left = newNode('b')

S.left.left = newNode('c')
S.right = newNode('d')


print(check_is_subtree(S, T))
    
    
