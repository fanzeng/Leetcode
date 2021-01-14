class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        self.l_morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s_morse = set()
        for word in words:
            s_morse.add(self.getMorse(word))
        return len(s_morse)

    def getMorse(self, word):
        morse = ''
        for char in word:
            morse += self.l_morse[ord(char) - ord('a')]
        return morse


