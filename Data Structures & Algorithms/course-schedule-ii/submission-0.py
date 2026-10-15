class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adjList[u].append(v)

        takeable = set()
        result = []

        def dfs(course: int, visited: set[int]) -> bool:
            if course in takeable:
                return True
            if course in visited:
                return False
            visited.add(course)

            for pre in adjList[course]:
                if not dfs(pre, visited):
                    return False
            takeable.add(course)
            result.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i, set()):
                return []
        return result

