# https://leetcode.com/problems/sort-characters-by-frequency/description/

# sorted method


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_char = {}
        for c in s:
            freq_char[c] = freq_char.get(c, 0) + 1

        sorted_freq = sorted(freq_char.items(), key=lambda x: x[1], reverse=True)

        result = "".join(ch * count for ch, count in sorted_freq)

        return result


# bucket sort method


class Solution:
    def frequencySort(self, s: str) -> str:
        tree = {}

        for c in s:
            tree[c] = tree.get(c, 0) + 1

        bucket = [[] for _ in range(len(s) + 1)]

        for ch, count in tree.items():
            bucket[count].append(ch)

        result = []

        for freq in range(len(bucket) - 1, 0, -1):
            for ch in bucket[freq]:
                result.append(ch * freq)

        return "".join(result)
