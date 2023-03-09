# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dic = defaultdict(int)
        def helper(root):
            if not root:
                return
            
            helper(root.left)
            dic[root.val] += 1
            helper(root.right)
        
        helper(root)
        
        arr = list(dic.values())
        if not arr:
            return []
        
        maxVal = max(arr)
        res = []
        for key in dic:
            if dic[key] == maxVal:
                res.append(key)
        
        return res
        