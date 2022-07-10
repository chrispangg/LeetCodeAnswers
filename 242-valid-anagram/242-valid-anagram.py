# check if length the same, return false if not
# turn into charArray
# sort the array
# for loop: if the str1[i] is not str2[i] return false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        strList1 = sorted(list(s))
        strList2 = sorted(list(t))
        for i, item in enumerate(strList1):
            if(strList1[i] != strList2[i]):
                return False
        return True