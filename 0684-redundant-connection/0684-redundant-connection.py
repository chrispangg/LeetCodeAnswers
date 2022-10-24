class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        cycle = set()
        
        def dfs(u, v):
            if u in cycle: return True
            if u == v: return False
            
            cycle.add(u)
            
            for i in graph[u]:
                if not dfs(i, v): return False
        
            cycle.remove(u)
            return True
        
        res = []
        for u, v in edges:
            if not dfs(u, v):
                res.append([u, v])
            
            graph[u].append(v)
            graph[v].append(u)
        
        return res[-1]