#input = 2 #output = [1,3,0,2], [2,0,3,1]

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        subset = []
        
        def backtrack(r):
            if len(subset) == n:
                subsetStr = subset_to_string()
                res.append(subsetStr)
                return
            
            for c in getCandidates():
                subset.append(c)
                backtrack(c)
                subset.pop()
        
        def getCandidates():
            position = len(subset)
            # candidates are the potential column it can be in
            candidates = set(range(n))

            for row, col in enumerate(subset):
                # discard candidates if it's in the same column
                candidates.discard(col)
                dist = position - row
                # discard diagonals
                candidates.discard(col + dist)
                candidates.discard(col - dist)

            return candidates
        
        def subset_to_string():
            # ex. [1, 3, 0, 2]
            # output: [".Q..","...Q","Q...","..Q."]
            ret = []
            for i in subset.copy():
                string = '.' * i + 'Q' + '.' * (n - i - 1)
                ret.append(string)
            return ret
        
        backtrack(0)
        return res
    
    
                    
    
        
    
            
            
            