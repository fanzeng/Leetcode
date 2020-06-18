class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list_pattern = list(pattern)
        list_str = str.split(' ')
        # print list_pattern, list_str
        if len(list_pattern) != len(list_str):
            return False
        dp = {}
        ds = {}
        for p, s in zip(list_pattern, list_str):
            if dp.get(p) is None:
                dp[p] = s
            else:
                if s != dp.get(p):
                    return False
            if ds.get(s) is None:
                ds[s] = p
            else:
                if p != ds.get(s):
                    return False
        return True

test = Solution()
print test.wordPattern("abba", "dog cat cat dog") # True
print test.wordPattern("abba", "dog cat cat fish") # False
print test.wordPattern("aaaa", "dog cat cat dog") # False
print test.wordPattern("abba", "dog dog dog dog") # False