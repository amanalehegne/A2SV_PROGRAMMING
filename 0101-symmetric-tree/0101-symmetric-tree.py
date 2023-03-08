# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def rec(leftSide, rightSide):
            
            if not leftSide or not rightSide:
                # If one side exists and the other doesn't it is not symetrical
                return not (leftSide or rightSide)
            
            if leftSide.val != rightSide.val:
                return False
                
            left = rec(leftSide.left, rightSide.right)
            right = rec(leftSide.right, rightSide.left)
            
            return (left and right)
            
        
        return rec(root.left, root.right)
            
            
            
            
        