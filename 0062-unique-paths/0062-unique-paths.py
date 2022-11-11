class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        graph = [[0]* n for i in range(m)]
        
        def dfs(i, j):
            if (i >= m or j >= n): return 0
            if i == m - 1 and j == n - 1: return 1
            if graph[i][j]: return graph[i][j]
            
            graph[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            
            return graph[i][j]
        
        return dfs(0, 0)