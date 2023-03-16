# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left=-float("inf"), right=float("inf")):
            if not root:
                return True
            
            if root.val >= right or root.val <= left:
                return False
            
            left = helper(root.left, left, root.val)
            right = helper(root.right, root.val, right)
            
            return left and right
            
        res = helper(root)
        return res