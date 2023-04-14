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
                return val
            
            count = 0
            if root.right:
                path.append(str(root.val))
                count += DFS(root.right, path)
                path.pop()
            if root.left:
                path.append(str(root.val))
                count += DFS(root.left, path)
                path.pop()
            
            return count
        
        return DFS(root, [])
                
        