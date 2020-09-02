class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.active_stems = []
        self.longest = max([len(word) for word in words])
        self.same_letter_count = 1
        self.previous_letter = ''
        self.same_letter_res = {}

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        if letter == self.previous_letter:
            self.same_letter_count += 1
        else:
            self.same_letter_count = 1
        if self.same_letter_count > self.longest:
            return self.same_letter_res[letter]
        self.previous_letter = letter
        is_word, node = self.trie.search(letter)
        res = is_word
        active_stems = [[node, 1]]
        for stem in self.active_stems:
            is_word, node = self.trie.searchFromNode(stem[0], letter)
            if is_word:
                res = True
            if stem[1]+1 < self.longest and node is not None:
                active_stems.append([node, stem[1]+1])
        self.active_stems = active_stems
        if self.same_letter_count == self.longest:
            self.same_letter_res[letter] = res
        return res

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

    # the search methods return the search result (T or F) as well as the node if it does not terminate
    def search(self, word):
        if word is None or len(word) == 0:
            return True, None
        return self._search(self.root, word)

    def searchFromNode(self, node, word):
        return self._search(node, word)

    def _search(self, node, word):
        if node is None:
            return False, None
        if len(word) == 0:
            return node.is_word, node
        if node.next.get(word[0]) is None:
            return False, None
        else:
            return self._search(node.next[word[0]], word[1:])

obj0 = StreamChecker(["cd","f","kl"])
print obj0.query('a') # False
print obj0.query('b') # False
print obj0.query('c') # False
print obj0.query('d') # True
print obj0.query('e') # False
print obj0.query('f') # True
print obj0.query('g') # False
print obj0.query('h') # False
print obj0.query('i') # False
print obj0.query('j') # False
print obj0.query('k') # False
print obj0.query('l') # True

obj1 = StreamChecker(["ab","ba","aaab","abab","baa"])
print obj1.query('a') # False
print obj1.query('a') # False
print obj1.query('a') # False
print obj1.query('a') # False
print obj1.query('a') # False
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('b') # False
print obj1.query('b') # False
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('b') # False
print obj1.query('b') # False
print obj1.query('b') # False
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('a') # True
print obj1.query('a') # False
print obj1.query('b') # True
print obj1.query('a') # True
print obj1.query('a') # True
print obj1.query('a') # False
