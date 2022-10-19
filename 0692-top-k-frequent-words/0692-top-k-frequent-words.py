class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        
        bucket = [None] * len(words)
        
        for i in count:
            if not bucket[count[i]]:
                arr = []
                arr.append(i)
                bucket[count[i]] = arr
            else:
                bucket[count[i]].append(i)
                
        res = []
        print(bucket)
        for i in range(len(words)):
            word_list = bucket.pop()
            if word_list:
                sortedlist = sorted(word_list)[::-1]
                while sortedlist and len(res) < k:
                    val = sortedlist.pop()
                    res.append(val)
        return res
                
        
            
        