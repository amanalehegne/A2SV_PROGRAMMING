from typing import List

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        def DFS(node, visited, parent):
            visited[node] = True
            for child in adj[node]:
                if not visited[child]:
                    check = DFS(child, visited, node)
                    if check:
                        return True
                elif child != parent:
                    return True
            return False
        
        visited = [False] * V
        for i in range(V):
            if not visited[i]:
                check = DFS(i, visited, -1)
                if check:
                    return True
        return False



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends