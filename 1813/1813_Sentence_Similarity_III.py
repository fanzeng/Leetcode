class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        """
        :type sentence1: str
        :type sentence2: str
        :rtype: bool
        """
        if sentence1 == sentence2:
            return True
        return self.isSimilar(sentence1, sentence2) or self.isSimilar(sentence2, sentence1)

    def isSimilar(self, s1, s2):
        if len(s1) < len(s2):
            return False # Assume s1 is longer than s2
        w1 = s1.split(" ")
        w2 = s2.split(" ")
        # Find the start of the section to remove from s1
        i = 0
        while w1[i] == w2[i]:
            i += 1
            if i == len(w2):
                return True
        # At this point, w1[i] is the first word that is different from w2[i]
        # From here onwards, there must be an index j such that w1[j:] == w2[i:]
        j = i + 1
        while j < len(s1):
            if self.isListEqual(w1[j:], w2[i:]):
                return True
            j += 1
        return False

    def isListEqual(self, a1, a2):
        if len(a1) != len(a2):
            return False
        for i in range(len(a1)):
            if a1[i] != a2[i]:
                return False
        return True
