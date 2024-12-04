class Solution {
    public boolean canMakeSubsequence(String str1, String str2) {
        int i = 0, j = 0;
        while (i < str1.length()) {
            char c1 = str1.charAt(i);
            char c2 = str2.charAt(j);
            char cn = getNextChar(c1);
            if (c1 == c2 || cn == c2) {
                j++;
                // System.out.printf("c1, cn, c2 = %c, %c, %c\n", c1, cn, c2);
            }
            if (j == str2.length()) return true;
            i++;
        }
        return false;
    }
    private char getNextChar(char c) {
        if (c == 'z') return 'a';
        return (char) ++c;
    }
}
