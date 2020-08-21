class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words = S.split(' ')
        res = ''
        for i, word in enumerate(words):
            res += ' '
            if word[0] in 'aeiouAEIOU':
                res += word + 'ma'
            else:
                res += word[1:] + word[0] + 'ma'
            res += 'a'*(i+1)
        return res[1:]

test = Solution()
print test.toGoatLatin("I speak Goat Latin") # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
print test.toGoatLatin("The quick brown fox jumped over the lazy dog") # "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"

