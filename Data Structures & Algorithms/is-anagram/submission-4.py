class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            SMap = {}
            TMap = {}

            for i in range(len(s)):
                SMap[s[i]] = 1 + SMap.get(s[i], 0)
                TMap[t[i]] = 1 + TMap.get(t[i], 0)
        return SMap == TMap

