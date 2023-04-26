# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        level = 1
        res = []
        while queue:
            sum_ = 0
            count = 0
            for i in range(level):
                node = queue.popleft()
                sum_ += node.val
                count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level = len(queue)
            res.append(sum_ / count)
                
            
        return res
        