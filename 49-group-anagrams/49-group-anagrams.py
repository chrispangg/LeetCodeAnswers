class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {} #str:list<str>, where str is the sorted
        
        for s in strs:
            sortedStr = "".join(sorted(s))
            if sortedStr in strMap:
                strMap[sortedStr].append(s)
            else:
                strMap[sortedStr] = [s]
        
        return strMap.values()
        
                
            