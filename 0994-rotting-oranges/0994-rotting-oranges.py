class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh, time = 0, 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        visited = set()
        directions = [[1, 0],[-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r >= 0 and c >= 0 and 
                        r < rows and c < cols and 
                        grid[r][c] == 1 and
                        (r, c) not in visited):
                        
                        grid[r][c] = 2
                        visited.add((r, c))
                        q.append((r, c))
                        fresh -= 1
            time += 1
                

        return time if fresh == 0 else -1
        
        
        
            
        
        