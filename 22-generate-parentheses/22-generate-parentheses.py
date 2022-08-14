"""
Backtracking - traverse for all solutions
["((()))","(()())","(())()","()(())","()()()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def backtrack(openN, closeN, n):
            if openN == closeN == n:
                group = "".join(temp)
                print(group)
                res.append(group)
                return
            
            if openN < n and openN >= closeN:
                temp.append("(")
                backtrack(openN + 1, closeN, n)
                temp.pop()
            
            if closeN < n and openN >= closeN:
                temp.append(")")
                backtrack(openN, closeN + 1, n)
                temp.pop()
            
            
        backtrack(0,0,n)
        return res    