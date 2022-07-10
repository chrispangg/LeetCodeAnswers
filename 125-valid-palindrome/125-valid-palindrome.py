# 1. remove space and comma, fullstop
# 2. two pointers - compare the first and last
# beware that the -1 is the last digit, but the first digit is 0
class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string = string + c.lower()
        
        #Alternative: string = ''.join(e for e in s if e.isalnum()).lower()
        
        for i, ele in enumerate (string):
            if string[i] != string[(i * -1) - 1]:
                    return False       
        return True