class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def createChildren(node_str):
            node = list(node_str)
            children = []
            for i in range(4):
                val = int(node[i])
                node[i] = str((val + 9) % 10) # Subtract 1
                children.append("".join(node))
                node[i] = str((val + 1) % 10) # Add 1 to the original
                children.append("".join(node))
                node[i] = str(val)

            return children


        def BFS(node, target, seen):
            queue = deque([(node, 0)])

            while queue:
                currentNode, level = queue.popleft()
                if currentNode not in seen:
                    if currentNode == target:
                        return level
                    seen.add(currentNode)
                    neighbours = createChildren(currentNode)
                    for neighbour in neighbours:
                        if neighbour not in seen:
                            queue.append((neighbour, level + 1))
            return -1

        seen = set(deadends)
        return BFS('0000', target, seen)