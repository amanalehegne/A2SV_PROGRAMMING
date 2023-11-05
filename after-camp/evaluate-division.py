class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
      def dijkstra(graph, scores, start, end):
            scores[start] = 1
            visited = set()

            priority_queue = [(1, start)]

            while priority_queue:
                current_score, current_node = heapq.heappop(priority_queue)
                if current_node == end:
                    return scores[end]

                if current_node in visited:
                    continue
                visited.add(current_node)

                for neighbor, score in graph[current_node]:

                    score = current_score * score
                    if score < scores[neighbor]:
                        scores[neighbor] = score

                    heapq.heappush(priority_queue, (score, neighbor))
            
            return -1




      graph = defaultdict(list)
      size = len(equations)

      score = dict()
      for i in range(size):
        graph[equations[i][0]].append((equations[i][1], values[i]))
        graph[equations[i][1]].append((equations[i][0], 1 / values[i]))
      
      for key in graph:
        score[key] = float('inf')

      res = []
      for start, end in queries:
        x = -1
        dic = copy.deepcopy(score)
        if start in score and end in score:
          x = dijkstra(graph, dic, start, end)
        
        res.append(x)
      
      return res
      


        