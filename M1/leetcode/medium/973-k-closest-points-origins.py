# https://leetcode.com/problems/k-closest-points-to-origin/description/

# initial solution


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result = list(map(lambda x: (x[0] ** 2 + x[1] ** 2), points))

        result_val = []

        for i in range(len(points)):
            result_val.append([points[i], result[i]])

        result_val = sorted(result_val, key=lambda x: x[1])

        result_val = [x[0] for x in result_val]

        return result_val[:k]


# optimised solution


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        result_val = [((p[0] ** 2 + p[1] ** 2), p) for p in points]

        result_val = sorted(result_val)

        return [j for i, j in result_val[:k]]
