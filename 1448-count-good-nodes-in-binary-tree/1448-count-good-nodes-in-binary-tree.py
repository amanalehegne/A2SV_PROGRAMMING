# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def helper(root, maxVal = -float("inf")):
            if not root:
                return
            if root.val >= maxVal:
                res[0] += 1
                maxVal = root.val
            helper(root.left, maxVal)
            helper(root.right, maxVal)
        
        helper(root)
        return res[0]