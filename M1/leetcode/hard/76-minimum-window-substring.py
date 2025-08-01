# https://leetcode.com/problems/minimum-window-substring/description/


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        target = {}
        for i in t:
            target[i] = target.get(i, 0) + 1

        window = {}

        have = 0
        need = len(target)
        res = [-1, -1]
        rlen = float("inf")
        left = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in target and window[s[right]] == target[s[right]]:
                have += 1

            while have == need:

                if (right - left + 1) < rlen:
                    res = [left, right]
                    rlen = right - left + 1

                window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        return s[res[0] : res[1] + 1] if rlen != float("inf") else ""
