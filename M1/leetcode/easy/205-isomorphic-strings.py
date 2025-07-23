# https://leetcode.com/problems/isomorphic-strings/description/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        hash = {}
        mapped = set()

        for i in range(len(t)):

            if s[i] not in hash:

                if t[i] in mapped:
                    return False

                hash[s[i]] = t[i]
                mapped.add(t[i])

            elif hash[s[i]] != t[i]:
                return False

        return True
