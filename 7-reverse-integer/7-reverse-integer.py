class Solution:
    def reverse(self, x: int) -> int:
        xStr = str(abs(x))
        reversedR = int(str(xStr[::-1]))
        if reversedR > 2147483647:
            return 0
        if x < 0:
            reversedR = reversedR * -1
        
        return reversedR