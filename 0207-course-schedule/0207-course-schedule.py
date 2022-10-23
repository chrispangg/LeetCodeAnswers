class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)
        
        visited = set()
        
        def dfs(c):
            if c in visited: return False
            if not preMap[c]: return True
            
            visited.add(c)
            for p in preMap[c]:
                if not dfs(p): return False
            visited.remove(c)
            preMap[c] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
            
        return True

        