class Solution:
    from collections import deque
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        order = []
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1
        queue = deque(node for node in range(len(indegree)) if indegree[node] == 0)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                if indegree[neighbor] > 0:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
    
        return order if len(order) == n else []


        