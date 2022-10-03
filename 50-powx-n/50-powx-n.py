class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def power(y, m):
            if y == 0: return 0
            if m == 0: return 1
            
            res = power(y * y, m//2)

            return y * res if m % 2 == 1 else res

        
        return power(x, abs(n)) if n >= 0 else 1/power(x, abs(n))
        