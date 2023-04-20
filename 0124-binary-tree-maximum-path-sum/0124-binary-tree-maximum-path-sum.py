# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_ = [-float("inf")]
        def DFS(node):
            if not node:
                return 0
            
            left = DFS(node.left)
            right = DFS(node.right)
            
            if left < 0:
                left = 0
            if right < 0:
                right = 0
                
            pathSum = left + right + node.val

            max_[0] = max(max_[0], pathSum)
            return node.val + max(left, right)
            
        DFS(root)
        return max_[0]
        