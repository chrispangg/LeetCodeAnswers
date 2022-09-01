class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # use deque because we want to popleft
        tickets.sort()
        adj = {u: collections.deque() for u, v in tickets}
        for u, v in tickets: adj[u].append(v)
        res = ["JFK"]
        
        def dfs(curr):
            if len(res) == len(tickets) + 1:
                return True
            if curr not in adj:
                return False
            
            for v in list(adj[curr]):
                #remove from adj[curr] and add to v to res
                adj[curr].popleft()
                res.append(v)
                if dfs(v): 
                    return res
                #if dfs didn't go well, 
                # pop v out from res and then add it back to adj[curr]
                res.pop() 
                adj[curr].append(v)
            return False
        
        dfs("JFK")
        return res