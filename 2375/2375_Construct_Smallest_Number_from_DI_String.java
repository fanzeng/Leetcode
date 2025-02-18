class Solution {
    public String smallestNumber(String pattern) {
        String ans = "999999999";
        int avail = 1111111110;
        for (int i = 1; i < 10; i++) {
            Optional<String> res = dp(pattern, i, avail - (int)Math.pow(10, i));
            if (res.isPresent())  {
                return i + res.get();
            }
        }
        return ans;
    }
    private Optional<String> dp(String pat, int prev, int avail) {
        if (pat.length() == 0) return Optional.of("");
        // System.out.printf("pat = %s, avail = %d\n", pat, avail);
        char c = pat.charAt(0);
        pat = pat.substring(1);
        if (c == 'I') {
            for (int j = prev+1; j < 10; j++)  {
                Optional<String> op = tryDigit(pat, avail, j);
                if (op.isPresent()) return op;
            }
        } else {
            for (int j = 1; j < prev; j++)  {
                Optional<String> op = tryDigit(pat, avail, j);
                if (op.isPresent()) return op;
            }
        }
        return Optional.empty();
    }
    private Optional<String> tryDigit(String pat, int avail, int j) {
        if ((int)(avail / Math.pow(10, j)) % 10 == 0) return Optional.empty();
        Optional<String> op = dp(pat, j, avail - (int)Math.pow(10, j));
        if (op.isPresent()) {
            return Optional.of(j + op.get());
        }
        return Optional.empty();
    }
}
