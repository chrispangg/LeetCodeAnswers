class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        res = []
        one = 1
        i = len(digits) - 1
        
        while digits:
            # print(str(digits[i]))
            
            digit = digits.pop() + one
            
            if digit >= 10:
                digit = digit % 10
                res.append(digit)
                
                if i == 0:
                    res.append(1)
                
            else:
                one = 0
                res.append(digit)
            
            i -= 1
            
            print(str(res))
                
        return reversed(res)
            