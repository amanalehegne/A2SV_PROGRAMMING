# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        def helper(root, level=1):
            if not root:
                return 0

            res[level].append(root.val)

            left = helper(root.left, level+1)
            right = helper(root.right, level+1)

            return max(left, right) + 1
        
        helper(root)
        
        return list(res.values())[::-1]
        