class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Idea is basically, if a node has any inbound edge, is has been beaten
        # Nodes without inbound edges aren't beaten
        # If there is one unbeaten team, return its number, if not, return -1
        #
        # Time: O(n + m), need to update beaten[] m times, need to run through beaten length n
        # Space: O(n), need to track if every team has been beaten in boolean array

        beaten = [False] * n
        for n1, n2 in edges:
            beaten[n2] = True
        
        validChampion = False
        teamNumber = -1
        
        for i, result in enumerate(beaten):
            if not result:
                if validChampion: 
                    return -1
                teamNumber = i
                validChampion = True

        return teamNumber 
    
    

