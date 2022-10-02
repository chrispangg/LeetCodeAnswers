class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        while l < r and t < b:
            #from top left to top right
            for i in range(r - l):
                res.append(matrix[t][l + i])
            
            #from top right to bottom right
            for i in range(b - t):
                res.append(matrix[t + i][r])
            
            
            #from bottom right to bottom left 
            for i in range(r - l):
                res.append(matrix[b][r - i])
            
            
            #from bottom left to top right 
            for i in range(b - t):
                res.append(matrix[b - i][l])
        
            #all pointers move inwards
            l += 1
            r -= 1
            t += 1
            b -= 1
        
        #edge case: when the last/inside is either a single row/col or cell, perform linear row scan to get remaining cells
        if len(res) < len(matrix[0]) * len(matrix):
            for i in range(t, b + 1):
                for j in range(l, r + 1):
                    res.append(matrix[i][j])
        return res