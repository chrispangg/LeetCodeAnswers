class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use deque because we want to popleft
        tickets.sort()
        adj = {src: collections.deque() for src, dst in tickets}
        for src, dst in tickets: 
            adj[src].append(dst)
            
        res = ["JFK"]
        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            if curr not in adj:
                return False
            
            # use a copy of adj[curr] so we can actually alter the list
            # as we loop
            for v in list(adj[curr]):
                #remove from adj[curr] and add to v to res
                adj[curr].popleft()
                res.append(v)
                
                if dfs(v): return res
                #if dfs didn't go well, 
                # pop v out from res and add it back to adj[curr]
                res.pop() 
                adj[curr].append(v)
            return False
        
        dfs("JFK")
        return res