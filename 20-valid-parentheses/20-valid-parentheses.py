# Use a map for the parentheses
# Use a stack to keep track of what's on top
# If can't get the given parenthese does not match the value of the map, then return false
# If map is empty, also return false

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1 : 
            return False
        
        p = {"{" : "}", "[" : "]", "(" : ")"}
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in p:
                stack.append(s[i])
                continue
                
            if len(stack) == 0:
                return False

            val = stack.pop()
            if p[val] != s[i]:
                return False
        
        
        return not stack