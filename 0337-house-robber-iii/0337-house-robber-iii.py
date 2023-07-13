# from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def rec(root, dic):
            if not root:
                return 0

            if root in dic:
                return dic[root]

            stepTwo = root.val

            if root.left:
                stepTwo += rec(root.left.left, dic)
                stepTwo += rec(root.left.right, dic)

            if root.right:
                stepTwo += rec(root.right.right, dic)
                stepTwo += rec(root.right.left, dic)
            
            stepOne = rec(root.left, dic) + rec(root.right, dic)

            dic[root] = max(stepOne, stepTwo)
            return dic[root]

        return rec(root, {})