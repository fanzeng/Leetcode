class Solution(object):
    stack = []
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s)):
            # print s[i]
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                self.stack.append(s[i])
            elif s[i] == ')':
                if len(self.stack) > 0 and self.stack[-1] == '(':
                    print self.stack.pop(), s[i]
                else:
                    return False
            elif s[i] == ']':
                if len(self.stack) > 0 and self.stack[-1] == '[':
                    print self.stack.pop(), s[i]
                else:
                    return False
            elif s[i] == '}':
                if len(self.stack) > 0 and self.stack[-1] == '{':
                    print self.stack.pop(), s[i]
                else:
                    return False
            else:
                return False
        if len(self.stack) > 0:
            return False
        return True


def main():
    test = Solution()
    print test.isValid(']')
    print test.isValid('()()([]({}()))')

if __name__ == '__main__':
    main()