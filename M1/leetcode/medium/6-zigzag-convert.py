# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = [""] * numRows

        curr_row = 0
        go_down = False

        for i in s:

            rows[curr_row] += i

            if curr_row == 0:
                go_down = True

            elif curr_row == numRows - 1:
                go_down = False

            if go_down:
                curr_row += 1
            else:
                curr_row -= 1

        return "".join(rows)
