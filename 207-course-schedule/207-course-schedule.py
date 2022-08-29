class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            preMap[c].append(p)
        
        visit, cycle = set(), set()
        
        def dfs(c):
            if c in cycle: return False
            if c in visit: return True
            
            cycle.add(c)
            
            for p in preMap[c]:
                if not dfs(p): return False
            cycle.remove(c)
            visit.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
            
        return True
                
            
            
            
            
        
        