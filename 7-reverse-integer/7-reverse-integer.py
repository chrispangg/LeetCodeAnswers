class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) == 1: return x
        tmp = x
        x = abs(x)
        res = x % 10
        x = x // 10
        for i in range(len(str(x))):
            if res > 2**31//10:
                return 0
            res = res * 10 + x % 10
            x = x //10
        
        return res if tmp > 0 else res * -1
    