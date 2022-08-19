class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subsets = []
        
        def backtrack(i):
            if i >= len(s):
                res.append(subsets.copy())
                return
            
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    subsets.append(s[i:j+1])
                    backtrack(j + 1)
                    subsets.pop()

        backtrack(0)
        return res
            
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True