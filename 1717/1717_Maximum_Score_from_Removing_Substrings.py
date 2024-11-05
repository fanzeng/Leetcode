from collections import deque
class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        if x > y:
            score_0, s = self.gain(s, x, 'ab')
            score_1, _ = self.gain(s, y, 'ba')
        else:
            score_0, s = self.gain(s, y, 'ba')
            score_1, _ = self.gain(s, x, 'ab')
        return score_0 + score_1

    def gain(self, s, reward, key):
        stack = deque()
        score = 0
        k0, k1 = key
        for c in s:
            # print stack
            stack.append(c)
            while len(stack) >= 2:
                if stack[-2] == k0 and stack[-1] == k1:
                    score += reward
                    stack.pop()
                    stack.pop()
                else:
                    break
        # print score, stack
        return score, stack
