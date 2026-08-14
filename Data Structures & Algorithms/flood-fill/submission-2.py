class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # if the element in question is the same as start upon start, edit. Only horizontally or vertially not diagonally
        #[
        # [1,1,1],
        # [1,1,0],
        # [1,0,1]
        # ]
        el = image[sr][sc]
        visited = set((sr,sc))
        cols = len(image[0])
        rows = len(image)
        stack = [(sr,sc)]
        directions = [(0,-1),(0,1),(-1,0),(1,0)]
        while stack:
            r,c = stack.pop()
            visited.add((r,c))
            image[r][c] = color
            for dr,dc in directions:
                if (0 <= r + dr < rows and 0 <= c + dc < cols) and (image[r+dr][c+dc] == el) and (((r+dr, c+dc)) not in visited):
                    stack.append((r+dr, c+dc))
        return image
            





