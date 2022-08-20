class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        subset = []
        dMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(i):
            # base case
            if i == len(digits):
                res.append("".join(subset[:]))
                return
            
                        
            for j in range(len(dMap[digits[i]])):
                subset.append(dMap[digits[i]][j])
                backtrack(i+1)
                subset.pop()
        
        backtrack(0)
        return res if digits else []