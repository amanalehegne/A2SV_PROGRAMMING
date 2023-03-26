# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        # Normal Binary Tree Insertion
        """
        Steps:
        1) Search The Binary Tree
        2) Insert it There
        """
        
        def bstSearch(prev, root, key):
            if not root:
                return prev
            
            if key < root.val:
                return bstSearch(root, root.left, key)
            else:
                return bstSearch(root, root.right, key)
        
        root = TreeNode(preorder[0])
        length = len(preorder)
        
        for i in range(1, length):
            val = preorder[i]
            par = bstSearch(None, root, val)
            node = TreeNode(val)
            if val > par.val:
                par.right = node
            else:
                par.left = node
        
        return root
        
        