class Solution:
    import heapq
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        for i in range(len(points)):
            adj[i] = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                distance = abs(x2-x1) + abs(y2-y1)
                adj[i].append([j,distance])
                adj[j].append([i,distance])

        totalCost = 0
        visited = set()
        visited.add(0)
        minHeap = []
        for edge in adj[0]:
            node2, weight = edge
            heapq.heappush(minHeap, [weight, 0, node2])
        while minHeap and len(visited) < len(points):
            weight, node1, node2 = heapq.heappop(minHeap)
            if node2 in visited:
                continue
            visited.add(node2)
            totalCost += weight

            for node, weight in adj[node2]:
                if node in visited:
                    continue
                heapq.heappush(minHeap,[weight,node2, node])
        return totalCost

        



