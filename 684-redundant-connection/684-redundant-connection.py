class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        n = len(edges)
        visit = set()
        
        def dfs(u,v):
            if u in visit:
                return False
            if u == v:
                return True
            visit.add(u)
            
            for i in graph[u]:
                if dfs(i, v):
                    return True
            
            visit.remove(u)
            
            return False
        
        res = []
        for u, v in edges:
            if dfs(u, v):
                res.append([u, v])
            
            graph[u].append(v)
            graph[v].append(u)
            
        return res[-1] #return the latest