import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        shortest = 0
        visited = set()
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for u,v,w in times:
            adj[u].append([v,w])
        print(adj)
        
        minHeap = [[0,k]]
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            shortest = w1
            
            for n2, w2 in adj[n1]:
                heapq.heappush(minHeap,[w2+w1, n2])
        print(visited)
        return shortest if len(visited) == n else -1





    

        