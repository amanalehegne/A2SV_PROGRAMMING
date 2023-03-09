# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumVal = [0]
        def helper(root):
            if not root:
                return
            
            right = helper(root.right)
            sumVal[0] += root.val
            root.val = sumVal[0]
            left = helper(root.left)
        
        helper(root)
        return root