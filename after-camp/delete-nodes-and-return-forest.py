# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []

        def dfs(node, is_root):
            if not node:
                return None

            remove = node.val in to_delete

            if is_root and not remove:
                res.append(node)

            node.left = dfs(node.left, remove)
            node.right = dfs(node.right, remove)

            return None if remove else node

        dfs(root, is_root=True)
        return res
