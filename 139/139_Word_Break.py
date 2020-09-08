class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.s = s
        self.res = []
        self.d = {}
        self.trie = Trie()
        for word in wordDict:
            self.trie.insert(word)
        return self.wordBreakDP(0)

    def wordBreakDP(self, word_begin):
        if word_begin == len(self.s):
            return True
        if self.d.get(word_begin) is not None:
            return self.d[word_begin]
        i = word_begin
        while i < len(self.s):
            word = self.s[word_begin:i+1]
            if self.trie.search(word):
                if self.wordBreakDP(i+1):
                    self.d[word_begin] = True
                    return True # break when found
            i += 1
        self.d[word_begin] = False
        return False

class TrieNode(object):
    def __init__(self):
        self.next = {}
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None or len(word) == 0:
            return
        self._insert(self.root, word)

    def _insert(self, node, word):
        char = word[0]
        if node.next.get(char) is None:
            node.next[char] = TrieNode()
        if len(word) == 1:
            node.next[char].is_word = True
        else:
            self._insert(node.next[char], word[1:])

    def search(self, word):
        if word is None or len(word) == 0:
            return True
        return self._search(self.root, word)

    def _search(self, node, word):
        if len(word) == 0:
            return node.is_word
        if node.next.get(word[0]) is None:
            return False
        else:
            return self._search(node.next[word[0]], word[1:])

test = Solution()
print test.wordBreak("leetcode", ["leet", "code"]) # True
print test.wordBreak("applepenapple", ["apple", "pen"]) # True
print test.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) # False
print test.wordBreak("a", ["a"]) # True
