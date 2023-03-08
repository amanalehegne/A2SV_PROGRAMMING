# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def helper(root):
            nonlocal res
            if not root:
                return [None, 0] 
                
            left = helper(root.left)
            right = helper(root.right)
            
            if left[0] == root.val:
                left[1] += 1
            else:
                left[1] = 0
            
            if right[0] == root.val:
                right[1] += 1
            else:
                right[1] = 0
            
            res = max(res, left[1] + right[1])
            
            return [root.val, max(left[1], right[1])]
        
        helper(root)
        return res