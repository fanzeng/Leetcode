class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.characters = characters
        self.combination_length = combinationLength
        if self.characters is not None and len(self.characters) > 0 and combinationLength > 0:
            self.has_ended = False
        else:
            self.has_ended = True
        self.combination = range(self.combination_length)
        self.final_combination = range(len(self.characters)-self.combination_length, len(self.characters))

    def next(self):
        """
        :rtype: str
        """
        if self.has_ended:
            return None
        res = ''.join([self.characters[i] for i in self.combination])
        if self.combination == self.final_combination:
            self.has_ended = True
        else:
            self.combination = self.getNextCombination(self.combination, len(self.characters)-1)
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return not self.has_ended

    def getNextCombination(self, l, max_index):
        if l[-1] + 1 <= max_index:
            l[-1] += 1
        else:
            l = self.getNextCombination(l[:-1], max_index - 1)
            l.append(l[-1]+1)
        return l

obj = CombinationIterator("abc", 2)
while obj.hasNext():
    print obj.next()

obj = CombinationIterator("abcdefghij", 5)
while obj.hasNext():
    print obj.next()

obj = CombinationIterator("", 0)
while obj.hasNext():
    print obj.next()
