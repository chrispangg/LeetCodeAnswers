class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False #char:node


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(node, substring):
            for i, c in enumerate(substring):
                # need to recursively call on every node in charcter map
                if c == ".":
                    for node in node.children.values():
                        if dfs(node, substring[i+1:]):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            return node.end
        
        
        return dfs(self.root, word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)