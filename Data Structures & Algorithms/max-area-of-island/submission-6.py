class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        rows = len(grid)
        cols = len(grid[0])
        stack = []
        visited = set()
        curr = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    stack.append((row,col))
                    visited.add((row,col))
                    while stack:
                        r,c = stack.pop()
                        curr += 1
                        for dr, dc in directions:
                            if(0 <= r + dr < rows and 0 <= c + dc < cols) and (grid[r+dr][c+dc] == 1) and ((r+dr, c+dc) not in visited):
                                stack.append((dr+r, dc +c))
                                visited.add((dr+r,c+dc))
                            else:
                                continue
                    result = max(result,curr)
                    curr = 0
        return result

        # grid=[
        #     [1,1,0,0,0],
        #     [1,1,0,0,0],
        #     [0,0,0,1,1],
        #     [0,0,0,1,1]]


        