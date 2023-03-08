# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            if not p or not q:
                return not(p or q)
            if p.val != q.val:
                return False
            left = helper(p.left, q.left)
            right = helper(p.right, q.right)
            
            return (left and right)
        
        return helper(p, q)
    
        