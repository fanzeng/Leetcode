from collections import deque
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.reverse(s)

    def reverse(self, s):
        stack = deque()
        for i, c in enumerate(s):
            if c == ')':
                res = ''
                while True:
                    a = stack.pop()
                    if a == '(':
                        break
                    res += a
                for c in res:
                    stack.append(c)
            else:
                stack.append(c)
        # print stack
        return ''.join(stack)
