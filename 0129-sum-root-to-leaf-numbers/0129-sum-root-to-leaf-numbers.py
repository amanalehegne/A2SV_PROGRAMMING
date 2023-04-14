# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def DFS(root, path):
            if not root.left and not root.right:
                path.append(str(root.val))
                val = int("".join(path))
                path.pop()
                res[0] += val
                return
                
            if root.right:
                path.append(str(root.val))
                DFS(root.right, path)
                path.pop()
            if root.left:
                path.append(str(root.val))
                DFS(root.left, path)
                path.pop()
        
        DFS(root, [])
        return res[0]
                
        