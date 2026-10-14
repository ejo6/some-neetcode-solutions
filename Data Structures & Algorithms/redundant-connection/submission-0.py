class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # there are len(edges) nodes in the graph
        parent = [i for i in range(n + 1)] 
        rank = [1] * (n + 1)
        
        def find(node: int):
            while node != parent[node]:
                parent[node] = parent[parent[node]] # little optimization
                node = parent[node]
            return node

        def union(node1: int, node2: int):
            parent1, parent2 = find(node1), find(node2)
            # This edge is redundant
            if parent1 == parent2: 
                return False
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parent[parent1] = parent2
                rank[parent2] += rank[parent1]
            return True

        for node1, node2 in edges:
            if not union(node1, node2): return [node1, node2]
        
        

        # Construct the graph using union find. 
        # When joining for an edge, if the two parents are the same, it's redundant.
        # Make the the most recent redundant edge, and continue union-finding