class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # --- Union Find ---
        parent = [i for i in range(n)]
        rank = [1] * n
        components = n

        def find(node: int) -> int:
            while node != parent[node]:
                parent[node] = parent[parent[node]] # path compression
                node = parent[node]
            return node

        def union(node1: int, node2: int) -> bool:
            nonlocal components

            parent1, parent2 = find(node1), find(node2)
            
            # The graph is cyclic
            if parent1 == parent2: return True

            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            components -= 1
            return False

        for u, v in edges:
            if union(u, v): return False
        
        return components == 1


        # # --- DFS ---
        # # Create an adjancency list
        # adjList = {i:[] for i in range(n)}
        # for u, v in edges:
        #     adjList[u].append(v)
        #     adjList[v].append(u)

        # visited = set()

        # def cyclic(node: int, parent: int) -> bool:
        #     visited.add(node)
            
        #     for neighbour in adjList[node]:
        #         if neighbour == parent: continue
        #         if neighbour in visited or cyclic(neighbour, node): 
        #             return True 
        #     return False
        
        # # If we found a cycle, return false
        # if cyclic(0, -1): return False

        # # Check if we've visited every node (1 component)
        # return len(visited) == n
        
        