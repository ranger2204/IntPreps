class Node:
    def __init__(self, char):
        self.char = char
        self.end_node = False
        self.links = {}

class Trie:
    def __init__(self):
        self.root = Node("")
        
    def add(self, word):
        cur = self.root
        for c in word:
            if c in cur.links:
                cur = cur.links[c]
            else:
                new_node = Node(c)
                cur.links[c] = new_node
                cur = new_node
        cur.end_node = True
        
    def word_from_dict(self, word):
        cur = self.root
        
        def recur(cur, word, index):
            if index >= len(word):
                return cur.end_node
            else:
                c = word[index]
                if c in cur.links:
                    l = recur(cur.links[c], word, index+1)
                    r = False
                    if not l and cur.end_node:
                        r = recur(self.root, word, index+1)
                    return l or r
                else:
                    if cur.end_node:
                        return recur(self.root, word, index)
                    return False
        return recur(cur, word, 0)

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        t = Trie()
        for w in wordDict:
            t.add(w)
        
        return t.word_from_dict(s)
        
tests = [
    {
        's': "leetcode",
        'wordDict': ["leet","code"]
    },
    {
        's': "catsandog",
        'wordDict': ["cats","dog","sand","and","cat"]
    },
    {
        's': 'cars',
        'wordDict': ['cars','ca','rs']
    }
]

for t in tests:
    print(t['s'], Solution().wordBreak(**t))