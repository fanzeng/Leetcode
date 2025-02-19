class Solution {
    public String getHappyString(int n, int k) {
        k--;
        // For n > 0, Total number of happy string of length n is 2^(n-1)*3
        if (k >= Math.pow(2, n - 1) * 3)
            return "";
        return dp(n, k, "");
    }

    private String dp(int n, int k, String prev) {
        if (n == 1)
            return getInitialLetter(k, prev);
        int d = (int) Math.pow(2, n - 1); // total number of happy strings of length n-1 given first letter.
        int q = k / d;
        String first = getInitialLetter(q, prev);
        int r = k % d;
        return first + dp(n - 1, r, first);
    }

    private String getInitialLetter(int q, String prev) {
        char[] letters = { 'a', 'b', 'c' };
        for (char letter : letters) {
            if (!String.valueOf(letter).equals(prev)) {
                if (q == 0) {
                    return String.valueOf(letter);
                }
                q--;
            }
        }
        return "";
    }
}
