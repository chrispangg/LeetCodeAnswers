class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # 1. create adjacency list, node:[neighbour nodes]
        adj = defaultdict(list)
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                node = grid[r][c]                   
                if c + 1 < cols: adj[node].append(grid[r][c + 1])
                if c - 1 >= 0: adj[node].append(grid[r][c - 1])
                if r + 1 < rows: adj[node].append(grid[r + 1][c])
                if r - 1 >= 0: adj[node].append(grid[r - 1][c]) 
        print(adj)
        
        # 2. Perform Dijkstra's Algorithm
        start = grid[0][0]
        target = grid[rows - 1][cols - 1]
        visited = set()
        minHeap = [[start, start]]
        
        while minHeap:
            totalcost, node = heapq.heappop(minHeap)
                
            if node == target: 
                return totalcost
            
            if node in visited: continue
            
            visited.add(node)
            
            for nei in adj[node]:
                if nei > totalcost: 
                    heapq.heappush(minHeap, [nei, nei])
                else:
                    heapq.heappush(minHeap, [totalcost, nei])
        