class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def BFS(node, seen=set()):
            keys = rooms[node]
            seen.add(node)
            count = 1
            for key in keys:
                if key not in seen:
                    count += BFS(key)
            
            return count
        
        return BFS(0) == len(rooms)