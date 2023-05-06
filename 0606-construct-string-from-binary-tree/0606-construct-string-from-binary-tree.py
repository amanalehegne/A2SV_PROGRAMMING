# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def DFS(root):
            if not root:
                return ""
            
            val = [str(root.val)]
            if not root.left and not root.right:
                return "".join(val)
            
            left = DFS(root.left)
            val.append("(")
            val.append(left)
            val.append(")")
            
            if root.right:
                right = DFS(root.right)
                val.append("(")
                val.append(right)
                val.append(")")
                
            return "".join(val)
        
        return DFS(root)
        