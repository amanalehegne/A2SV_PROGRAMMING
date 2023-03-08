# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sumVal = 0
        def rightSum(root):
            nonlocal sumVal
            if not root:
                return 
            sumVal += root.val
            left = rightSum(root.left)
            right = rightSum(root.right)
        
        def helper(root):
            nonlocal sumVal
            if not root:
                return
            
            helper(root.left)
            
            tempVal = root.val
            root.val = sumVal
            sumVal -= tempVal
            
            helper(root.right)
            
        
        
        rightSum(root)
        helper(root)
        return root
        