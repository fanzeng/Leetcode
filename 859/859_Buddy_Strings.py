class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return self.hasDuplicateLetters(A)
        count, diff = self.countDiff(A, B)
        # print count, diff
        if count == 2:
            return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


    def hasDuplicateLetters(self, s):
        d = {}
        for char in s:
            if d.get(char) is not None:
                return True
            d[char] = 1
        return False
    
    def countDiff(self, A, B):
        count = 0
        diff = []
        for a, b in zip(A, B):
            if a != b:
                count += 1
                diff.append((a, b))
        return count, diff
        
        
        
