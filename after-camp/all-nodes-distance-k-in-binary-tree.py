# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                nextNode = node.left
                graph[node.val].append(nextNode.val)
                graph[nextNode.val].append(node.val)
                stack.append(nextNode)
            if node.right:
                nextNode = node.right
                graph[node.val].append(nextNode.val)
                graph[nextNode.val].append(node.val)
                stack.append(nextNode)
        
        
        def BFS(graph, root, seen, k):
            queue = deque([root])
            level = 0
            res = []
            while queue:
                size = len(queue)
                for _ in range(size):
                    node = queue.popleft()
                    if node not in seen:
                        if level == k:
                            res.append(node)
                        if level > k:
                            return res
                        seen.add(node)
                        children = graph[node]
                        for child in children:
                            if child not in seen:
                                queue.append(child)
                level += 1
            return res
        
        seen = set()
        return BFS(graph, target.val, seen, k)