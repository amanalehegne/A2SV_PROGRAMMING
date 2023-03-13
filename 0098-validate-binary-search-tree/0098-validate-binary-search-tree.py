# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def helper(root):
            if not root: 
                return
            left = helper(root.left)
            arr.append(root.val)
            right = helper(root.right)
        
        def isSorted(arr):
            length = len(arr)
            for i in range(length - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            
            return True
        
        helper(root)
        return isSorted(arr)