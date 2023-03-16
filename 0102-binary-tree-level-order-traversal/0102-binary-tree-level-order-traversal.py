# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def helper(root, level = 0):
            if not root:
                return
            dic[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root)
        return list(dic.values())