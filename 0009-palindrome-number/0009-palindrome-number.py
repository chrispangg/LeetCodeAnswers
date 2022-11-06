class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        strx = str(x)
        l, r = 0, len(strx) - 1
        while l < r:
            if strx[l] != strx[r]: 
                return False
            l += 1
            r -= 1
        return True
        