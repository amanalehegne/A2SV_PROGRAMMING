# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def DFS(root):
            if not root:
                return 0
            res = 0
            if root.val % 2 == 0:
                if root.left and root.left.left:
                    res += root.left.left.val
                if root.left and root.left.right:
                    res += root.left.right.val
                if root.right and root.right.left:
                    res += root.right.left.val
                if root.right and root.right.right:
                    res += root.right.right.val
            left = DFS(root.left)
            right = DFS(root.right)
            return left + right + res
        

        return DFS(root)
                