class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i, num in enumerate(tokens):
            if num == "+" or num == "-" or num == "*" or num == "/":
                top = stack.pop()
                lastTop = stack.pop()
                res = eval(str(lastTop + num + top))
                stack.append(str(int(res)))
            else:
                stack.append(num)
                
        return stack[0]