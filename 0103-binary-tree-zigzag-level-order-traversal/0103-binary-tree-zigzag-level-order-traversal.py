# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        state = True
        res, temp = [], []
        size = 1
        while queue and queue[-1]:
            current = queue.popleft()
            temp.append(current.val)
            
            if len(temp) == size:
                if not state:
                    temp.reverse()
                res.append(temp)
                temp = []
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            
            # One Level end and the other began
            if not temp:
                size = len(queue)
                state = not state
        
        return res
            