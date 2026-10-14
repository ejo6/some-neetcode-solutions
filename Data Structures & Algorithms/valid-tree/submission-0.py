class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # --- DFS ---
        # Create an adjancency list
        adjList = {i:[] for i in range(n)}
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def cyclic(node: int, parent: int) -> bool:
            visited.add(node)
            
            for neighbour in adjList[node]:
                if neighbour != parent and neighbour in visited: 
                    return True 
                if neighbour != parent: 
                    if cyclic(neighbour, node): return True
            return False
        
        # If we found a cycle, return false
        if cyclic(0, 0): return False

        # Check if we've visited every node (1 component)
        return len(visited) == n
        
        