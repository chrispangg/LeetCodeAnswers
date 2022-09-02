class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # craete weighted graph in adj map i:[cost, nei nodes]
        adj = {i:[] for i in range(n + 1)}
        for node, nei, cost in times:
            adj[node].append([cost, nei])
        print(adj)
        
        time = 0
        visited = set()
        minHeap = [[0,k]]
        
        while minHeap:
            cost, node = heapq.heappop(minHeap)
            if node in visited: continue
            visited.add(node)
            time = max(time, cost)
            for cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, [time + cost, nei])
        
        return time if len(visited) == n else -1
            
        