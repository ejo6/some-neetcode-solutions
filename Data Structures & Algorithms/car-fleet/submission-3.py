class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time = -(-(target - position[i]) // speed)

        cars = sorted(zip(position, speed), reverse=True)
        times = []
        
        for position, speed in cars:
            time = (target - position) / speed
            times.append(time) # push how long it will take for the car to get there

        result = 0
        curr = 0
        for time in times: 
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


