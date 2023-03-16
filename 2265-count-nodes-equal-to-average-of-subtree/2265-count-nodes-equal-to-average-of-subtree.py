# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def helper(root):
            if not root:
                return [0, 0]
        
            left = helper(root.left)
            right = helper(root.right)
            
            sumVal = left[0] + right[0] + root.val
            nodeCount = left[-1] + right[-1] + 1
            
            if sumVal // nodeCount == root.val:
                res[0] += 1
            
            return [sumVal, nodeCount]
        
        helper(root)
        return res[0]
        