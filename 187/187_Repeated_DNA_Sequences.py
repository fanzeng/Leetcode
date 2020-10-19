class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 11:
            return []
        self.d = {}
        res = []
        for i in xrange(len(s)-9):
            substr = s[i:i+10]
            if self.d.get(substr) is None:
                self.d[substr] = 1
            elif self.d[substr] == 1:
                self.d[substr] = 2
                res.append(substr)
        return res

test = Solution()
print test.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT') # ["AAAAACCCCC","CCCCCAAAAA"]
print test.findRepeatedDnaSequences('AAAAAAAAAAAAA') # ["AAAAAAAAAA"]

