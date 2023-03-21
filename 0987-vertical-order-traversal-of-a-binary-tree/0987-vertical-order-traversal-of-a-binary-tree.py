# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        def helper(node, row, col):
            if not node:
                return
            dic[col].append((row, node.val))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)
        
        helper(root, 0, 0)
        res = []
        for k in sorted(dic):
            column = [val for row, val in sorted(dic[k])]
            res.append(column)
            
        return res
        