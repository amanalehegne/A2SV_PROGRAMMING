# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def helper(gp, p, c):
            nonlocal res
            if not c: 
                return

            if gp and not gp.val % 2:
                res += c.val
            left = helper(p, c, c.left)
            right = helper(p, c, c.right)
        
        helper(None, None, root)
        
        return res
    