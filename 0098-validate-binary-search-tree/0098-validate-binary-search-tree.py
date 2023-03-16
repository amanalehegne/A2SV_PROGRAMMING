# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-float("inf")]
        ans = [True]
        def helper(root):
            if not root:
                return
            helper(root.left)
            
            if prev[0] >= root.val:
                ans[0] = False
                return
            
            prev[0] = root.val
            
            helper(root.right)
        helper(root)
        return ans[0]