"""
Create a charMap and a stack
add the key value to stack if str[i] in key i.e. if str[i] == "{", then add "}" to stack
else, check if the top of stack is equal to str[i] i.e. if str[i] == "}", check if the top of the stack is "}". If it's not, return false
i.e. {,[,(,),],},}
"""
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        charMap = {"{": "}", "(": ")", "[": "]"}
        
        for c in s:
            if c in charMap:
                stack.append(charMap[c])
            elif stack:
                p = stack.pop() 
                if c != p:
                    return False
            else:
                return False
                    
        
        if len(stack) > 0: 
            return False
        
        return True