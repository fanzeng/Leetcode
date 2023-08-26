class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.d = {}
        return self.isInterLeaveRecursive(s1, s2, s3) or self.isInterLeaveRecursive(s2, s1, s3)

    def isInterLeaveRecursive(self, s1, s2, s3):
        h = self.getHash(s1, s2, s3)
        if self.d.get(h) is not None:
            return self.d[h]
        if len(s3) == 0:
            res = len(s1) == 0 and len(s2) == 0
            self.d[h] = res
            return res
        if len(s3) == 1:
            res = (len(s2) == 0 and len(s1) == 1 and s3[0] == s1[0]) or (len(s1) == 0 and len(s2) == 1 and s3[0] == s2[0])
            self.d[h] = res
            return res
        if len(s1) == 0 or s1[0] != s3[0]:
            self.d[h] = False
            return False
        i = 0
        res = False
        while i < len(s1) and i < len(s3) and s1[i] == s3[i]:
            res = res or self.isInterLeaveRecursive(s2, s1[i+1:], s3[i+1:])
            i += 1
        self.d[h] = res
        return res
    
    def getHash(self, s1, s2, s3):
        return s1 + '_' + s2 + '_' + s3
