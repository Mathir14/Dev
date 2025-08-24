# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# initial solution


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result = [points[0]]

        for i in range(1, len(points)):
            if points[i][0] <= result[-1][1]:
                result[-1][1] = min(result[-1][1], points[i][1])
            else:
                result.append(points[i])

        return len(result)


# optimised solution


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        arrow = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > arrow:
                count += 1
                arrow = points[i][1]
        return count
