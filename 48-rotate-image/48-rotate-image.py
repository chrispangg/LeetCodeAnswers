class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r #same because it's a squre matrix
                
                # save the topleft temp variable
                topLeft = matrix[top][l + i] # +i to shift right
                
                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l] #-i to shift up
                
                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i] #-i to shift left
                
                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r] 
                
                # move top left into top right
                matrix[top + i][r] = topLeft
            
            r -= 1
            l += 1
        