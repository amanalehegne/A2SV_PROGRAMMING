# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 or not root2:
                return not(root1 or root2)
            if root1.val != root2.val:
                return False
            left = sameTree(root1.left, root2.left)
            right = sameTree(root1.right, root2.right)
            
            return left and right
        
        def findNode(root1, root2):
            if not root1 or not root2:
                return False

            if root1.val == root2.val:
                res = sameTree(root1, root2)
                if res:
                    return res
            
            left = findNode(root1.left, root2)
            right = findNode(root1.right, root2)
            return left or right
        
        return findNode(root, subRoot)
        