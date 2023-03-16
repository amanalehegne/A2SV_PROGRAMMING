# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(preorder, inorder):
            if not preorder and not inorder:
                return None
            
            parent = preorder[0]
            parentNode = TreeNode(parent)
            partition = inorder.index(parent)
            
            left = helper(preorder[1:partition + 1], inorder[:partition])
            right = helper(preorder[partition + 1:], inorder[partition + 1:])
            
            parentNode.left = left
            parentNode.right = right
            
            return parentNode
        
        res = helper(preorder, inorder)
        return res
            
        