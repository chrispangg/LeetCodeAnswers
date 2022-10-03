class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        n_multiply, m_multiply = 1, 1
        
        for m in num2[::-1]: #45
            for n in num1[::-1]: #123
                res += int(m) * int(n) * n_multiply * m_multiply
                n_multiply = n_multiply * 10
            
            n_multiply = 1
            m_multiply = m_multiply * 10
            
        return str(res)
            
                
                
                