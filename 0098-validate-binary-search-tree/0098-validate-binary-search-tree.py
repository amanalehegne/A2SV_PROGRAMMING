# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-float("inf")]
        def helper(root):
            if not root:
                return True
            
            left = helper(root.left)
            
            if prev[0] >= root.val:
                return False
            prev[0] = root.val
            
            right = helper(root.right)
            
            return left and right
            
        res = helper(root)
        return res