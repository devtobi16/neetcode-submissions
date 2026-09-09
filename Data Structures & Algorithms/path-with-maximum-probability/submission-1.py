import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        visited = set()
        for i in range(n):
            graph[i] = []
        for (s, d), p in zip(edges, succProb):
            graph[s].append([d,p])
            graph[d].append([s,p])

        minHeap = [[1, start_node]]
        visited.add((1,start_node))
        while minHeap:
            p1, n1 = heapq.heappop(minHeap)
            if n1 == end_node:
                return -p1
            for n2, p2 in graph[n1]:
                if (-abs(p2*p1), n2) in visited:
                    continue
                heapq.heappush(minHeap,[-abs(p2*p1), n2])
                visited.add((-abs(p2*p1), n2)) 
        return 0

