"""
Append to Stack for every number.
When an operator appears, pop the last two number to perform operations
Then, replace tokens[i-2] with the new number returned, also save the new number in a variable
return the variable at the end of the loop

"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, num in enumerate(tokens):
            stack.append(num)
            
            if num == "+" or num == "-" or num == "*" or num == "/":
                # print(str(stack))
                symbol = stack.pop()
                top = stack.pop()
                lastTop = stack.pop()
                res = eval(str(lastTop + symbol + top))
                
                stack.append(str(int(res)))
        return stack[0]