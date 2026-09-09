class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)

        for s in strs:
            SortedS = ''.join(sorted(s))
            out[SortedS].append(s)
        return list(out.values())