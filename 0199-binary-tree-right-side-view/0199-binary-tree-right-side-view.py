# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        size = 1
        count = 0
        res = []
        while queue and queue[-1]:
            current = queue.popleft()
            count += 1
            if count == size:
                res.append(current.val)
                count = 0
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if not count:
                size = len(queue)
            
        return res
            
        