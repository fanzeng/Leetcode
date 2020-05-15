class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if word is None or len(word) == 0:
            return
        n = self.root
        i = 0
        while n is not None:
            next = n.children.get(word[i])
            if next is None:
                break
            else:
                n = next
            i += 1
            if i == len(word):
                break
        for j in xrange(i, len(word)):
            n.children[word[j]] = Node()
            n = n.children[word[j]]
        n.children['end'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word is None or len(word) == 0:
            return True
        n = self.root
        for c in word:
            next = n.children.get(c)
            if next is None:
                return False
            n = next
        return n.children.get('end') is True


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix is None or len(prefix) == 0:
            return True
        n = self.root
        for c in prefix:
            next = n.children.get(c)
            if next is None:
                return False
            n = next
        return True

class Node(object):
    def __init__(self, c=None):
        self.children = {}
        if c is not None:
            self.children[c] = Node()


obj = Trie()
obj.insert('apple')
print obj.search('apple') # T
print obj.search('app') # F
print obj.startsWith('app') # T
print obj.search('appl') # F
print obj.search('apply') # F
obj.insert('apply')
print obj.search('apply') # T
print obj.search("app") # F
print obj.startsWith("app") # T
obj.insert('app')
print obj.search("app") # T
print obj.startsWith("app") # T
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)