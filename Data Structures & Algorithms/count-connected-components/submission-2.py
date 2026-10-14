class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n
        
        components = n

        def find(node):
            # Could be recursive easily, iterative:
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Little optimization, not necessary
                node = parent[node]
            return node

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            # Same parent, don't union
            if parent1 == parent2: return 0 
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent[parent1]
                rank[parent1] += rank[parent2]
            else: 
                parent[parent1] = parent[parent2]
                rank[parent2] += rank[parent1]
            return 1

        for node1, node2 in edges:
            components -= union(node1, node2)

        return components





        # --- DFS METHOD ---
        # # Create adjList
        # adjList = {i:[] for i in range(n)}
        # for edge in edges:
        #     adjList[edge[0]].append(edge[1])
        #     adjList[edge[1]].append(edge[0])

        # visited = set()

        # def dfs(node: int) -> None:
        #     visited.add(node)

        #     for neighbour in adjList[node]:
        #         if neighbour not in visited:
        #             dfs(neighbour) 
        #     return

        # components = 0

        # for node in adjList.keys():
        #     if node not in visited:
        #         dfs(node)
        #         components += 1

        # return components

