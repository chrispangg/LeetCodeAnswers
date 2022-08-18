class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set() # use a set to keep track of our existing path so we don't walk back
        
        def backtrack(r, c, i): #position for row, column and word[i]
            if i == len(word):
                return True
            if (r < 0 or c < 0 or #when out of bound
                r >= ROWS or c >= COLS or #when out of bound another way
               word[i] != board[r][c] or #when the character is not in the current pos
               (r,c) in path): #when visiting the same position twice
                return False
            
            path.add((r,c))
            # recursively call for all directions and increment word[i] by 1
            # if any of them return true, our res will return true
            res = (backtrack(r + 1, c, i + 1) or
                  backtrack(r - 1, c, i + 1) or
                  backtrack(r, c + 1, i + 1) or
                  backtrack(r, c - 1, i + 1))
            
            # clean up the path 
            path.remove((r,c))
            
            return res
        
        # call backtrack on every position as starting position
        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r,c,0): return True
        
        return False