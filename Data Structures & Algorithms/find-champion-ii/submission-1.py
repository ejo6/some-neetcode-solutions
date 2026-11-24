class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
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
    
    

