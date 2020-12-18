class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens = sorted(tokens)
        # print tokens
        if len(tokens) < 1:
            return 0
        score = 0
        while len(tokens) > 0:
            min_token = tokens.pop(0)
            if P < min_token:
                return score
            else:
                score += 1
                P -= min_token
                # print 'min_token =', min_token, 'score =', score
                remain_token_sum = sum(tokens)
                # print 'remain_token_sum =', remain_token_sum, 'P =', P, 'score =', score
                if P >= remain_token_sum:
                    return score + len(tokens)
                remain_token_sum_but_last_1 = sum(tokens[:-1])
                if P >= remain_token_sum_but_last_1:
                    return score + len(tokens)-1
            if len(tokens) < 2:
                break
            max_token = tokens.pop()
            score -= 1
            # print 'max_token =', max_token, 'score =', score
            P += max_token
        return score


test = Solution()
print test.bagOfTokensScore([100], 50) # 0
print test.bagOfTokensScore([100,200], 150) # 1
print test.bagOfTokensScore([100,200,300,400], 200) # 2
print test.bagOfTokensScore([25,91], 99) # 1
print test.bagOfTokensScore([48,87,26], 81) # 2