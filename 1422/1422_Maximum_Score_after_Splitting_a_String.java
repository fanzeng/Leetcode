class Solution {
    public int maxScore(String s) {
        int zeroCount = 0;
        int oneCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                zeroCount++;
            } else {
                oneCount++;
            }
        }
        int score = -1;
        int zeros = 0;
        for (int i = 0; i < s.length()-1; i++) {
            if (s.charAt(i) == '0') {
                zeros++;
            }
            int sc = zeros + (oneCount - (i+1-zeros));
            if (sc > score) score = sc;
        }
        return score;
    }
}
