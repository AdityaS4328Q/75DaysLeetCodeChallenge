from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps=defaultdict(list)
        for s in strs:
            key="".join(sorted(s))
            grps[key].append(s)
        return list(grps.values())
        