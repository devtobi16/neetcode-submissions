class Solution:
    from collections import deque
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for prerequisite in prerequisites:
            course, req = prerequisite
            graph[req].append(course)
            indegree[course] += 1
        queue = deque(i for i in range(len(indegree)) if indegree[i] == 0)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in graph[node]:
                if indegree[neighbor] >= 1:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        return order if len(order) == numCourses else []
        