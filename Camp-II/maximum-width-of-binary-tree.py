# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 0])
        res  = 0
        
                        
        while queue:
            node1 = queue[0][1]
            node2 = queue[-1][1]
            
            res = max(res, node2 - node1 + 1)
            size = len(queue)
            for i in range(size):
                node, level = queue.popleft()
                
                if node.left:
                    queue.append((node.left, 2 * level))
                    
                if node.right:
                    queue.append((node.right, 2 * level + 1))
        
        
        return res
        