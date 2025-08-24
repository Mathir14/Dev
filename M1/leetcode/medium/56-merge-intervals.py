# https://leetcode.com/problems/merge-intervals/description/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]

        for interval in range(1, len(intervals)):
            if intervals[interval][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[interval][1])
            else:
                result.append(intervals[interval])

        return result
