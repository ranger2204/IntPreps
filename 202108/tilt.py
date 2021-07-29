# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def recur(root):
            nonlocal tilt
            if root is None:
                return 0

            sr = recur(root.right)
            sl = recur(root.left)
            tilt += abs(sr - sl)
            return sr+sl+root.val
        
        recur(root)
        return tilt