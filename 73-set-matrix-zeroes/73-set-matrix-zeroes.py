class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeros.add((r, c))
        
        # print(zeros) #row, cols {(0, 3), (0, 0)}
        for row, col in zeros:
            #update all values in the row
            for r in range(len(matrix)):
                matrix[r][col] = 0
                
            for c in range(len(matrix[0])):
                matrix[row][c] = 0    
        
        