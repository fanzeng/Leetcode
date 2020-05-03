class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True

        self.d = {
            "": True,
        }
        success, _ = self.check([], s)
        return success


    def check(self, stack, s):
        if s is None or len(s) == 0:
            if len(stack) == 0:
                return True, stack
            else:
                return False, stack
        # print 'checking:\n\t ', 'stack =', stack, ', s =', s
        stored = self.d.get(self.get_key(stack, s))
        if self.d.get(self.get_key(stack, s)) is not None:
            # print 'Successfully retrieved stored result.', self.get_key(stack, s), stored
            success, stack_str = stored
            stack = list(stack_str)
            return success, stack
        # else:
        #     print 'self.d =', self.d
        # print 'self.d =', self.d

        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
            elif c == ')':
                # print 'At s[' + str(i) + '], \')\' encountered, poping ', stack
                success, stack = self.popstack(stack)
                if not success:
                    # print 'Failed.'
                    self.save_result(stack, s, False)
                    return False, stack
            elif c == "*":
                # print 'At s[' + str(i) + '], \'*\' encountered, stack =', stack
                stack_old = stack
                if i == len(s)-1:
                    if len(stack) < 2:
                        return True, []
                    else:
                        return False, stack
                else:
                    s_remaining = s[i+1:]
                # print 'stack =', stack, 's_reminaing =', s_remaining
                success, stack_after = self.check(stack_old[:], s_remaining)
                self.save_result(stack_after, s_remaining, success)
                if success:
                    return True, stack_after

                success, stack_after = self.check(stack_old[:], '(' + s_remaining)
                self.save_result(stack_after, s_remaining, success)
                if success:
                    return True, stack_after

                success, stack_after = self.check(stack_old[:], ')'+ s_remaining)
                self.save_result(stack_after, s_remaining, success)
                if success:
                    return True, stack_after
                else:
                    return False, stack_old

        if len(stack) == 0:
            self.save_result(stack, s, True)
            self.d[self.get_key(stack, s)] = True, stack
            return True, stack
        else:
            self.save_result(stack, s, False)
            return False, stack

    def popstack(self, stack):
        if stack is None or len(stack) == 0:
            return False, stack

        if stack[-1] == '(':
            return True, stack[:-1]
        else:
            return False, stack

    def get_key(self, stack, s):
        return ''.join(stack) + s

    def save_result(self, stack, s, success):
        self.d[self.get_key(stack, s)] = success, ''.join(stack)


test = Solution()
print test.checkValidString("") # True
print test.checkValidString("()") # True
print test.checkValidString("()()()()()") # True
print test.checkValidString("()()()*)()") # True
print test.checkValidString("*)()()*)()") # True
print test.checkValidString("(()*()*)())") # True
print test.checkValidString("(()())((()())(()()))") # True
print test.checkValidString("(*)") # True
print test.checkValidString("(*))") # True
print test.checkValidString("()(())(((((()())(()))))()(*()))()()()()((()(())())*((((())))*())()(()()))*((()(()(()))))(()())(*(*") # True


print test.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())") # False
print test.checkValidString("(*)))") # False
print test.checkValidString("())") # False
print test.checkValidString("()()()()(()") # False

