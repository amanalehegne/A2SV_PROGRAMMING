# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        check = True
        def rec(leftSide, rightSide):
            nonlocal check
            
            if not leftSide or not rightSide:
                if leftSide or rightSide:
                    check = False
                return
            
            if leftSide.val != rightSide.val:
                check = False
                
            x = rec(leftSide.left, rightSide.right)
            y = rec(leftSide.right, rightSide.left)
        
        rec(root.left, root.right)
        
        return check
            
            
            
            
        