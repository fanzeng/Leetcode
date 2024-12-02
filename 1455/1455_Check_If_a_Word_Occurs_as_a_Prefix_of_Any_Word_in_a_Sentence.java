class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        char[] cs = sentence.toCharArray();
        char[] cw = searchWord.toCharArray();
        int i = 0;
        int w = 1;
        while (i < cs.length) {
            int j = 0;
            while (j < cw.length && i < cs.length && cw[j] == cs[i]) {
                i++; j++;
            }
            if (j == cw.length) {
                return w;
            } else {
                while (i < cs.length && cs[i] != ' ') i++;
                w++;
                i++;
            }
        }
        return -1;
    }
}
