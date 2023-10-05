class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
      graph = [[False] * n for _ in range(n)]
      for i, j in prerequisites:
          graph[i][j] = True


      for k in range(n):
          for i in range(n):
              for j in range(n):
                  graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])

      res = []
      for x, y in queries:
          res.append(graph[x][y])
      
      return res
        