# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dic = defaultdict(int)
        res = [0]
        
        def helper(root, count):
            if not root:
                return
            count += root.val
            
            if count == targetSum:
                res[0] += 1
            
            res[0] += dic[count - targetSum]
            
            dic[count] += 1
            
            helper(root.left, count)
            helper(root.right, count)
            dic[count] -= 1
            
            if dic[count] == 0:
                dic.pop(count)
                
            return
        
        helper(root, 0)
        return res[0]