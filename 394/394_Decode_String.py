class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        return self.decodeStringRecursive(s)[0]

    def decodeStringRecursive(self, s):
        # print 's =', s
        decoded = ''
        i = 0
        while i < len(s):
            char = s[i]
            # print 'i, s[i] =', i, s[i]
            if char == ']':
                return decoded, s[i+1:]
            if char >= 'a' and char <= 'z':
                decoded += char
                i += 1
                continue
            str_k = ''
            while char >= '0' and char <= '9':
                str_k += char
                i += 1
                char = s[i]
            k = int(str_k)
            # print 'k =', k
            i += 1 # skip [
            repeated, rest = self.decodeStringRecursive(s[i:])
            # print 'repeated =', repeated, 'rest =', rest
            for j in xrange(k):
                decoded += repeated
            s = rest
            i = 0
        return decoded, ''

test = Solution()
print test.decodeString("3[a]2[bc]") # "aaabcbc"
print test.decodeString("3[a2[c]]") # "accaccacc"
print test.decodeString("2[abc]3[cd]ef") # "abcabccdcdcdef"
print test.decodeString("abc3[cd]xyz") # "abccdcdcdxyz"