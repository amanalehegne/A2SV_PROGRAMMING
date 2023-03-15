# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root):
            if not root:
                return
            
            # This will swap the entire subtree
            """
              1
             / \
            3   4
            /\   \
            5 6   7
            
            if we swap 3 and 4 the tree will become
              1
             / \
            4   3
             \  /\
              7 5 6
            """
            temp = root.left
            root.left = root.right
            root.right = temp
            
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return root
            
        