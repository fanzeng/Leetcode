class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.cvtbksp(S) == self.cvtbksp(T)

    def cvtbksp(self, s):
        i = 0
        l = []
        for c in s:
            if c == '#':
                if i <= 1:
                    l = []
                    i = 0
                else:
                    l = l[:i-1]
                    i -= 1
            else:
                l.append(c)
                i += 1
        return ''.join(l)

test = Solution()
print test.backspaceCompare("ab#c", T = "ad#c") # Output: true
print test.backspaceCompare("ab##", T = "c#d#") # Output: true
print test.backspaceCompare("a##c", T = "#a#c") # Output: true
print test.backspaceCompare("a#c", T = "b") # Output: false
print test.backspaceCompare("c##vnvr", "c##vn#nvr") # Output: true
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.