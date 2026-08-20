from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        result = 0
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        visited = set()
        pathExists = False
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col] == 2) and ((row, col) not in visited):
                    queue.append((row,col))
                    visited.add((row,col))
        while queue:
            qLen = len(queue)
            for el in range(qLen):
                r,c = queue.popleft()
                for dr, dc in directions:
                    if ((0 <= r + dr < rows) and (0 <= c+dc < cols)) and ((r+dr, c+dc)not in visited) and (grid[r+dr][c+dc] == 1):
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
                        grid[r+dr][c+dc] = 2
                        pathExists = True
            if pathExists:
                result += 1
                pathExists = False
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

                    
        return result

                    

        