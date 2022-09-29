class Solution:
    def checkValidString(self, s: str) -> bool:
        
        minRemain, maxRemain = 0, 0
        
        for c in s:
            if c == "(":
                minRemain, maxRemain = minRemain + 1, maxRemain + 1
            elif c == ")":
                 minRemain, maxRemain = minRemain - 1, maxRemain - 1 
            else:
                 minRemain, maxRemain = minRemain - 1, maxRemain + 1
            if maxRemain < 0: #meaning we have an open parenthesis
                return False
            if minRemain < 0: #accomodate for too many stars
                minRemain = 0
        return minRemain == 0