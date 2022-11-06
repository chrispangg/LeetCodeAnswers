class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        word = ""
        shortest = 201
        for s in strs:
            if len(s) < shortest:
                word = s
                shortest = len(s)
        
        # if shortest == 0: return ""
        res = 0
        for i in range(len(word)):
            for s in strs:
                if s[i] != word[i]:
                    return word[:res]
            res += 1
        return word[:res]
            