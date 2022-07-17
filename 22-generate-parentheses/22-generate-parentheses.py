"""
Use backtracking because we want multiple solutions
Bounding conditions:
    - number of opens must equal to closes
    - open must be before closes
Therefore:
    - only add open paranthesis if open < n
    - only add a closing paranthesis if open > closed
    - valid IIF open == closed == n
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                print(str(stack))
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                #we pop it afterwards because the stack is reused after we added to res, so we have to clean it up for the next combo.
                stack.pop() 
                
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
            

        backtrack(0,0)
        return res