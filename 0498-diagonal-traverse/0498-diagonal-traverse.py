class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        y = len(mat)
        x = len(mat[0])
        state = True
        xIndex = yIndex = 0
        res = []
        resSize = 0
        
        while resSize < x*y:
            if state:
                while yIndex >= 0 and xIndex < x:
                    res.append(mat[yIndex][xIndex])
                    resSize += 1
                    
                    xIndex += 1
                    yIndex -= 1
                
                if xIndex == x:
                    yIndex += 1
                    xIndex -= 1
                yIndex += 1
            else:
                while yIndex < y and xIndex >= 0:
                    res.append(mat[yIndex][xIndex])
                    resSize += 1
                    
                    xIndex -= 1
                    yIndex += 1
                
                if yIndex == y:
                    yIndex -= 1
                    xIndex += 1
                xIndex += 1
            state = not state
        
        return res
                