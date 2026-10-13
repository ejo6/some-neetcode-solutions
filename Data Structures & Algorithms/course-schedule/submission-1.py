class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list
        adjList = {i:[] for i in range(numCourses)}
        for course, prerequisite in prerequisites:
            adjList[course].append(prerequisite)

        takeable = set()

        def dfs(visited: set(), course: int) -> bool:
            # We've detected a loop
            if course in takeable:
                return True
            if course in visited: 
                return False
            visited.add(course)
            for prerequisite in adjList[course]:
                if not dfs(visited, prerequisite): return False # cannot take course
            takeable.add(course)
            return True
        
        for index in range(numCourses):
            if not dfs(set(), index):
                return False
        return True



