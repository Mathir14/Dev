# https://leetcode.com/problems/car-pooling/


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001

        for passengers, pickups, drops in trips:
            stops[pickups] += passengers
            stops[drops] -= passengers

        current = 0
        for people in stops:
            current += people
            if current > capacity:
                return False

        return True
