class Solution(object):
    stack = []
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0,len(s)):
            # print s[i]
            if s[i] == '(':
                self.stack.append(s[i])
            elif s[i] == ')':
                if self.stack[len(self.stack)-1] == '(':
                    print self.stack.pop(), s[i]
                else:
                    return False
        if len(self.stack) > 0:
            return False
        return True


def main():
    test = Solution()
    print test.isValid('()()((()))')

if __name__ == '__main__':
    main()