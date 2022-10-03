class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False
        
        # determine which rows/cols need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    # set row or column (or rowZero) to zero
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        # zero out body of the matrix                
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # zero out the column header
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        # zero out the row header
        if rowZero == True:
            for c in range(cols):
                matrix[0][c] = 0
                
                    
                