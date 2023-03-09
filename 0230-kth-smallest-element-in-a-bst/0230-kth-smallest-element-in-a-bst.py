# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Count Variable
        count = [0, 0]
        def helper(root):
            if not root:
                return
            helper(root.left)
            count[0] += 1
            if count[0] == k:
                count[1] = root.val
            helper(root.right)
        
        
        helper(root)
        return count[1]
            
            
            
                
        