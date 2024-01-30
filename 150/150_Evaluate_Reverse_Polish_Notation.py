class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif t == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif t == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif t == '/':
                b = stack.pop()
                a = stack.pop()
                if a * b < 0:
                    stack.append(-(-a / b))
                else:
                    stack.append(a / b)
            else:
                stack.append(int(t))
        return stack[0]       
