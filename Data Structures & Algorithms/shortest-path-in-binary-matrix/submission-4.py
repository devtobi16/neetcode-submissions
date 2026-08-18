from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        length = 1
        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
        if grid[0][0] != 0:
            return -1
        queue = deque([(0,0)])
        visited = set()
        visited.add((0,0))
        while queue:
            queueL = len(queue)
            for el in range(queueL):
                r,c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
            
                for dr,dc in directions:
                    if ((0 <= dr + r < rows) and (0 <= dc + c < cols)) and ((r+dr, c+dc) not in visited) and (grid[r+dr][c+dc] == 0):
                        queue.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
            length += 1
        return -1

# [
#     [0,1,0,1,0],
#     [1,0,0,0,1],
#     [0,0,1,1,1],
#     [0,0,0,0,0],
#     [1,0,1,0,0]]

        