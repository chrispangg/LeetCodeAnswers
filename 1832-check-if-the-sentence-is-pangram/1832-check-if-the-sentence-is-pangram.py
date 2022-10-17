class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dic = {i: 0 for i in list(string.ascii_lowercase)}
        
        for c in sentence:
            if c.lower() in dic:
                dic[c] = dic[c] + 1
        for i in dic:
            if dic[i] < 1:
                return False
            
        return True
        
        
        