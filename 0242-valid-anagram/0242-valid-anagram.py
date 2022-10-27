class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        sCount = Counter(s)
        tCount = Counter(t)
        for c in sCount:
            if sCount[c] != tCount.get(c, 0):
                return False
        return True