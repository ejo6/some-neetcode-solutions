class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        
        result = 0
        curr = 0

        for position, speed in cars:
            time = (target - position) / speed
            if time > curr: 
                curr = time
                result += 1
        
        return result
        
        # s : 2 6 
        # 8 (n)
        # 7 (n-1)
        # 3 (n-2)
        # 6 ()
        # 8 doesnt catch
        # 7 doesnt cach
        # 3 and 3 will meet up
        # 3 and 3 will then collide with 6
        # 2 goes alone


