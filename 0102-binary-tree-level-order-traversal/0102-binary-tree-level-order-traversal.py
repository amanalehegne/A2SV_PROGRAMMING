# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        temp = []
        size = 1
        while queue and queue[-1]:
            current = queue.popleft()
            temp.append(current.val)
            if len(temp) == size:
                res.append(temp)
                temp = []
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if not temp:
                size = len(queue)
        
        return res