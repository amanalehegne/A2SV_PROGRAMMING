class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        count = [0]
        def BFS(node, seen=set()):
            keys = rooms[node]
            seen.add(node)
            for key in keys:
                if key not in seen:
                    count[0] += 1
                    BFS(key)
        
        BFS(0)
        return count[0] + 1 == len(rooms)