from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c,0))
        
        while queue:
            ar, ac, levelRes = queue.popleft()
            visited.add((ar,ac))
            if grid[ar][ac] == (2**31)-1:
                grid[ar][ac] = levelRes

            for dr, dc in directions:
                if (0 <= ar+dr < rows and 0 <= ac + dc < cols) and (grid[ar+dr][ac+dc] ==(2**31) -1) and ((ar+dr, ac+dc) not in visited):
                    queue.append((ar+dr, ac+dc, levelRes + 1))
                    visited.add((ar+dr,ac+dc))
                        
                 


