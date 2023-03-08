# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            if not p or not q:
                return not(p or q)
            if p.val != q.val:
                return False
            left = isSame(p.left, q.left)
            right = isSame(p.right, q.right)
            
            return (left and right)
        
        check = False
        def helper(root, subRoot):
            nonlocal check
            if not root or not subRoot:
                return not(root or subRoot)
            if root.val == subRoot.val:
                check = isSame(root, subRoot)
                if check: return check
            left = helper(root.left, subRoot)
            right = helper(root.right, subRoot)
                
            return (left or right)
                
        
        
        return helper(root, subRoot)
            
        