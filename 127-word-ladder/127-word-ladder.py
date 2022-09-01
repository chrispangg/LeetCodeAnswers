class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # generate pattern map
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for c in range(len(word)):
                pattern = word[:c] + "*" + word[c + 1:]
                nei[pattern].append(word)
        print(nei)
        # '*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot', 'hit'], 'ho*': ['hot'], 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog'], '*it': ['hit'], 'hi*': ['hit']

        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for c in range(len(word)):
                    pattern = word[:c] + "*" + word[c + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            q.append(neiWord)
            res += 1    
        return 0
        
                