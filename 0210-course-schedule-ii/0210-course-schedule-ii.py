class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        preMap = defaultdict(list)
        for c, p in prerequisites:
            preMap[c].append(p)
        
        visited, cycle = set(), set()
        
        def dfs(c):
            if c in visited: return True
            if c in cycle: return False
            
            cycle.add(c)
            
            for p in preMap[c]:
                if not dfs(p): return False
                
            cycle.remove(c)
            visited.add(c)
            
            res.append(c)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return res
            