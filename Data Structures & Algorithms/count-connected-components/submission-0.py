class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adjList
        adjList = {i:[] for i in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        visited = set()

        def dfs(node: int) -> None:
            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    dfs(neighbour) 
            return

        components = 0

        for node in adjList.keys():
            if node not in visited:
                dfs(node)
                components += 1

        return components

