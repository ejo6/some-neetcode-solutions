class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0: return True


        adjList = {i:set() for i in range(numCourses)}
        for u, v in prerequisites:
            # Use a set for easier removing (better for large graphs)
            adjList[u].add(v)

        takeable = set() 

        def dfs(node: int, visited: set[int]) -> bool:
            # If the course is takeable
            if node in takeable:
                return True
            # Check for cycle
            if node in visited: 
                return False
            visited.add(node)

            for pre in adjList[node]:
                if not dfs(pre, visited): return False
            takeable.add(node)
            return True

        for i in range(numCourses):
            if not dfs(i, set()): return False
        return True


        # for i in range(len(adjList)):
        #     if not dfs(i, set()): return False

        # Build adjacency list: {course:prerequisites}
        # Run a DFS through the first course to each prerequisite:
        #   if we find a cycle, return Fale
        #   if the recurse into a course with no prerequisites, return True
        #   remove that "True" from the parents prerequisite list
        # If at the end the length of the takeable courses is numCourses, return True
