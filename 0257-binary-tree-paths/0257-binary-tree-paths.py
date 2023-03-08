# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def helper(root, temp, res):
            if not root:                
                return False
            temp.append(str(root.val))
            
            left = helper(root.left, temp, res)
            right = helper(root.right, temp, res)
            
            if not left and not right:
                res.append("->".join(temp))
            temp.pop()
            return True
            
            
        arr = []
        res = []
        helper(root, arr, res)
        return res
        