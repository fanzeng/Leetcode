class TrieNode(object):
    def __init__(self):
        self.isWord = False
        self.next = {}
        for i in xrange(26):
            self.next[str(unichr(ord('a')+i))] = None

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.addWordToTrieNode(word, self.root)

    def addWordToTrieNode(self, word, node):
        if word is None or len(word) == 0:
            node.isWord = True
            return
        c = word[0]
        if node.next[c] is None:
            node.next[c] = TrieNode()
        self.addWordToTrieNode(word[1:], node.next[c])

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchFromTrieNode(word, self.root)

    def searchFromTrieNode(self, word, node):
        if word is None or len(word) == 0:
            return node.isWord
        c = word[0]
        if c == '.':
            for a in [str(unichr(ord('a')+i)) for i in xrange(26)]:
                if node.next[a] is not None and self.searchFromTrieNode(word[1:], node.next[a]):
                    return True
            return False
        if node.next[c] is None:
            return False
        return self.searchFromTrieNode(word[1:], node.next[c])


obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print obj.search("pad") # False
print obj.search("bad") # True
print obj.search(".ad") # True
print obj.search("b..") # True