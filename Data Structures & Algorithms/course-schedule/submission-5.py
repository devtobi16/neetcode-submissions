from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        indegree = [0]*numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        print(indegree)
        print(graph)
        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return completed == numCourses



