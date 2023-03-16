# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root):
            if not root:
                return []
            left = helper(root.left)
            left.append(root.val)
            right = helper(root.right)
            
            return left + right
        
        arr = helper(root)        
        return arr[k - 1]