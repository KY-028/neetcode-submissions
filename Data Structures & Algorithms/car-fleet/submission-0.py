class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [[position[i], speed[i]] for i in range(len(position))]
        pos_speed.sort(key=lambda x: x[0], reverse=True)

        fleets = 0
        stack = [(target - pos_speed[0][0]) / pos_speed[0][1]]
        for i in range(1, len(pos_speed)):
            
            # check if the next car catches up:
            if (target - pos_speed[i][0]) / pos_speed[i][1] <= stack[-1]:
                # this is a fleet with the previous car, no repeated push
                continue
            else:
                # not going to form a fleet, make a new
                stack.append((target - pos_speed[i][0]) / pos_speed[i][1])
        
        return len(stack)