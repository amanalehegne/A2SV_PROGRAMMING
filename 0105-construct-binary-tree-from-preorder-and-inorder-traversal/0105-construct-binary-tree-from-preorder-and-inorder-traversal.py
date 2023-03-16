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
            # The first element will be our parent node, and the very first element in preorder is the root node
            parentNode = TreeNode(parent)
            # LNR (left, node, right) if how we traverse inorder
            # This means if we find the the position of the current node, all element left to it will be placed in the left side and all the elements to the right will be in nodes right side
            partition = inorder.index(parent)
            
            # We partition the list into left and right recursively
            left = helper(preorder[1:partition + 1], inorder[:partition])
            right = helper(preorder[partition + 1:], inorder[partition + 1:])
            
            parentNode.left = left
            parentNode.right = right
            
            return parentNode
        
        res = helper(preorder, inorder)
        return res
            
        