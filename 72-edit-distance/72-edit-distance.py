class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #word1=rows, word2=cols -> dp[r][c]
        cache = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        #fill up the bottom row
        for i in range(len(word2) + 1):
            cache[len(word1)][i] = len(word2) - i
        #fill up the right most column
        for j in range(len(word1) + 1):
            cache[j][len(word2)] = len(word1) - j
        
        #Bottom up 
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = 1 + min(cache[i+1][j+1], cache[i][j+1], cache[i+1][j])
        
        return cache[0][0]
                    
        