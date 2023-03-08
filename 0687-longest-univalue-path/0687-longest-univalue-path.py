# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(par, root):
            nonlocal res
            if not root:
                return 0
                
            left = helper(root, root.left)
            right = helper(root, root.right)
            
            res = max(res, left + right)
            
            if not par or (root.val == par.val):
                return max(left, right) + 1
            return 0
        
        helper(None, root)
        return res