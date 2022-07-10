# 1. remove space and comma, fullstop
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(e for e in s if e.isalnum()).lower()
        for i, ele in enumerate (string):
            if string[i] != string[(i * -1) - 1]:
                    return False
                
        return True