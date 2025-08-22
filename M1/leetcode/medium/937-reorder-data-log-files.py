# https://leetcode.com/problems/reorder-data-in-log-files/description/


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            id, rest = log.split(" ", 1)
            if rest[0].isalpha():
                letter_logs.append((rest, id))
            else:
                digit_logs.append(log)

        letter_logs.sort()

        return [f"{id} {rest}" for rest, id in letter_logs] + digit_logs
