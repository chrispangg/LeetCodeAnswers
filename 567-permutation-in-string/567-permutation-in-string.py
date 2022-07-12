"""
s1 = oob  as2:  aobo
arr = [a,b], len(s1), r, l = 0, 0

find permutations of a substring within a sliding window.
Option 1: can use sort then compare substring with s1
Option 2 (recommended): compare using a map, they have must identical keys and values, where key = char, value = frequency
If substring matches with the map, return True. Else, we can remove the laftest key, then slide the window forward

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        #initalise charMap and subCharMap
        charMap, subCharMap = {}, {}
        for c in s1:
            charMap[c] = charMap.get(c, 0) + 1
            
            
        l = 0
        # loop s2
        for r in range (len(s2)):
            subCharMap[s2[r]] = subCharMap.get(s2[r], 0) + 1

            #compare length
            MapSize = 0
            subMapSize = 0
            for s in charMap.values():
                MapSize += s
            for s in subCharMap.values():
                subMapSize += s
            
            if MapSize == subMapSize:
                print(str(subCharMap) + " " + str(charMap))
                
                if charMap == subCharMap:
                    return True
                #compare charMap with subCharMap. If not match
                if subCharMap[s2[l]] > 1:
                    subCharMap[s2[l]] = subCharMap.get(s2[l]) - 1
                else:
                    del subCharMap[s2[l]]
                    
                l += 1
                
        return False
        