class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for node, nei, cost in times:
            adj[node].append([cost, nei])
            
        time = 0
        visited = set()
        minHeap = [[0, k]]
        
        while minHeap:
            # always pop the shortest path - O(log n) operation
            cost, node = heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            time = max(time, cost)
            
            for neiCost, nei in adj[node]:
                if nei in visited: continue
                heappush(minHeap, [time + neiCost, nei])
        
        return time if len(visited) == n else -1