class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        return self.longestSubStringDP(s, k)

    def longestSubStringDP(self, s, k):
        l_char_less_than_k = self.getListCharLessThanK(s, k)
        if len(l_char_less_than_k) == 0:
            return len(s)
        else:
            # print 'char less than k =', l_char_less_than_k
            char_less_than_k = l_char_less_than_k[0]
            l_substring = s.split(char_less_than_k)
            l_length = []
            for substring in l_substring:
                l_length.append(self.longestSubStringDP(substring, k))
            return max(l_length)

    def getListCharLessThanK(self, s, k):
        d_freq = {}
        for char in s:
            if d_freq.get(char) is None:
                d_freq[char] = 1
            else:
                d_freq[char] += 1
        return [item[0] for item in d_freq.items() if item[1] < k]


test = Solution()
print test.longestSubstring("aaabb", 3) # 3
print test.longestSubstring("ababbc", 2) # 5
print test.longestSubstring("aabbabacbababab", 4) # 0