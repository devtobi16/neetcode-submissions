import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = {}
        shortest = {}
        for i in range(n):
            graph[i] = []
        
        for u,v,w in edges:
            graph[u].append([v,w])

        minHeap = [[0, src]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in graph[n1]:
                heapq.heappush(minHeap, [w1 + w2, n2])
        for j in range(n):
            if j not in shortest:
                shortest[j] = -1
        return shortest




