# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def rec(node, isLeft):
            if not node:
                return 0
            if not node.left and not node.right:
                if isLeft:
                    return node.val
                return 0
            
            left = rec(node.left, True)
            right = rec(node.right, False)

            return left + right
        
        return rec(root, False)
        