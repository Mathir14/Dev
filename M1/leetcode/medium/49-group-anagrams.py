# https://leetcode.com/problems/group-anagrams/description/

# initial solution 

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if None in strs:
            return [strs]
        if len(strs) == 1:
            return [strs]
        result = []
        result.append([strs[0]])
        for i in strs[1:]:
            for j in range(len(result)):
                if Counter(i) == Counter(result[j][0]):
                    result[j].append(i)
                    break
                if j == len(result)-1:
                    result.append([i])
        return result
    
# sorted tuple

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for word in strs:
            key = tuple(sorted(word))
            anagrams[key].append(word)
        
        return list(anagrams.values())
