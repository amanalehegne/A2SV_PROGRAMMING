# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        def helper(root, level):
            if not root:
                return

            res[level].append(root.val)

            left = helper(root.left, level+1)
            right = helper(root.right, level+1)
        
        helper(root, 1)
        return list(res.values())
    