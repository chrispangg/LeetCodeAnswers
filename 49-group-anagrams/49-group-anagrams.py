class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {} #str:list<str>, where str is the sorted
        
        for s in strs:
            sortedStr = "".join(sorted(s))
            strMap[sortedStr] = strMap.get(sortedStr, []) + [s]

        return strMap.values()
        