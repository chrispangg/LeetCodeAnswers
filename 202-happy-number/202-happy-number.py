class Solution:
    def isHappy(self, n: int) -> bool:
        
        repeated = set()
        
        while True:
            if n == 1: return True
            
            if n in repeated:
                return False
            else:
                repeated.add(n)
                
            res = [int(a) for a in str(n)]
            n = 0
            for num in res:
                n += num**2
            
            print(str(n))
                
            
        
        return True
            
            
            