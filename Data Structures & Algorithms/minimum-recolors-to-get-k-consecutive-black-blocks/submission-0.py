class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # Iterate through the list with window size k
        # Track the number of W while sliding the winow
        # Take the min we wever saw

        l, r = 0, k
        best = 0

        for i in range(k):
            if blocks[i] == "W":
                best += 1
        
        inWindow = best
        
        while r < len(blocks):
            # If the next block is W, add to window
            if blocks[r] == "W":
                inWindow += 1
            # If the current block is white, were eviciting it
            if blocks[l] == "W":
                inWindow -= 1
            best = min(best, inWindow)
            l += 1; r += 1
        
        return best
        

            
