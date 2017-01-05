class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            # print s[i]
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    print stack.pop(), s[i]
                else:
                    return False
            elif s[i] == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    print stack.pop(), s[i]
                else:
                    return False
            elif s[i] == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    print stack.pop(), s[i]
                else:
                    return False
            else:
                return False
        if len(stack) > 0:
            return False
        return True

def main():
    test = Solution()
    print test.isValid(']')
    print test.isValid('()()([]({}()))')

if __name__ == '__main__':
    main()