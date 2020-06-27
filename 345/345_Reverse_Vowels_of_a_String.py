class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        is_vowel = []
        l_vowel = []
        res = ''
        for c in s:
            c_is_vowel = c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
            is_vowel.append(c_is_vowel)
            if c_is_vowel:
                l_vowel.append(c)
        l_vowel.reverse()
        vowel_count = 0
        for i, c in enumerate(s):
            if is_vowel[i]:
                res += l_vowel[vowel_count]
                vowel_count += 1
            else:
                res += c
        return res