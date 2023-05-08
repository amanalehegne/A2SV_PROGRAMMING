class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        def checkValidPosition(borad, node):
            return 0 <= node[0] < len(board) and 0 <= node[-1] < len(borad[0])
        
        def DFS(borad, root):
            stack = [root]
            seen = set()
            
            seen.add(root)
            res = True
            
            dir_ = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            
            while stack:
                node = stack.pop()
                
                for r, c in dir_:
                    nextNode = (node[0] + r, node[-1] + c)
            
                    if checkValidPosition(board, nextNode):
                        if borad[nextNode[0]][nextNode[-1]] == "O" and nextNode not in seen:
                            stack.append(nextNode)
                            seen.add(nextNode)
                    else:
                        res = False
            
            if res:
                for row, col in seen:
                    board[row][col] = "X"
        
        
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    DFS(board, (row, col))
                    
        
                
        