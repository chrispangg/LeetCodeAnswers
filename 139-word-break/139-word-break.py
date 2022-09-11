class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        #reverse
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # if string has enough words to compare with word and
                # the substring is the word, then we cache
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]: 
                    break
                    
        return dp[0]