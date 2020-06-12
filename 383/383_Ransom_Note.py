class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for c in ransomNote:
            if c not in magazine:
                return False
            else:
                pos = magazine.find(c)
                new_magazine = magazine[:pos]
                if pos + 1 < len(magazine):
                    new_magazine += magazine[pos+1:]
                magazine = new_magazine
        return True

test = Solution()
print test.canConstruct("a", "b")
print test.canConstruct("aa", "ab")
print test.canConstruct("aa", "aab")