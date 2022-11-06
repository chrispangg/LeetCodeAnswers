class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        strx = str(x)
        return strx == strx[::-1]
    
        