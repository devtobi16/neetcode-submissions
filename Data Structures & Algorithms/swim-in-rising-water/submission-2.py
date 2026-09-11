import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # maxVal = float('-inf')
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        minHeap = [(grid[0][0],(0,0))]
        while minHeap:
            currVal = heapq.heappop(minHeap)
            r,c = currVal[1]
            if (r,c) in visited:
                continue
            visited.add((currVal[1]))
            if r == rows - 1 and c == cols - 1:
                return currVal[0]
            for dr,dc in directions:
                if (0 <= dr + r < rows and 0 <= dc + c < cols) and ((r+dr, c+dc) not in visited):
                    heapq.heappush(minHeap,(max(currVal[0], grid[dr + r][dc + c]), (dr+r, dc+c)))
                else:
                    continue






                


      
        