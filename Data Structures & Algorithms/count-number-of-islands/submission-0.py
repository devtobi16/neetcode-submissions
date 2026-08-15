class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        stack= []
        visited = set()
        count = 0
        for row_start in range(rows):
            for col_start in range(cols):
                if grid[row_start][col_start] == "1" and ((row_start, col_start) not in visited):
                    count += 1
                    stack.append((row_start, col_start))
                    while stack:
                        r,c = stack.pop()
                        visited.add((r,c))
                        for dr, dc in directions:
                            if (0 <= r+ dr < rows and 0<= c + dc < cols) and (grid[r+dr][c+dc] == "1") and ((r+dr, c+dc) not in visited):
                                stack.append((dr + r, dc + c))
                else:
                    continue
        return count


                    


            
