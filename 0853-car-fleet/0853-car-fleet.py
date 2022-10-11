class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dic = {}
        for i in range(len(position)):
            dic[position[i]] = speed[i]
        position.sort()

        fleets = 0
        prev_car = -1
        for i in range(1, len(position) + 1):
            # arrival time is remaining distance divided by speed you're going
            # arrival time = (destination - current position) / speed
            # If two cars arrive at the same time, they are considered as a single fleet
            arrival_time = (target - position[-i]) / dic.get(position[-i])
            if arrival_time > prev_car:
                fleets += 1
                prev_car = arrival_time
        return fleets