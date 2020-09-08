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