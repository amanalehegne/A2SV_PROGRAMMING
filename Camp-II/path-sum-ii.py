# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def rec(node, arr, sumVal):
            if not node:
                return

            arr.append(node.val)
            
            if (not node.left and not node.right) and (sumVal + node.val == targetSum):
                res.append(arr[:])
            
            rec(node.left, arr, sumVal + node.val)
            rec(node.right, arr, sumVal + node.val)
            
            arr.pop()
        
        rec(root, [], 0)
        return res
