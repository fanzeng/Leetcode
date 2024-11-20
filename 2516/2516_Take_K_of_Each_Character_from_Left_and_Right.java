class Solution {
    public int takeCharacters(String s, int k) {
        if (k == 0) return 0;
        int countA = 0;
        int countB = 0;
        int countC = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == 'a') countA++;
            if (c == 'b') countB++;
            if (c == 'c') countC++;
        }
        // System.out.printf("countA = %d, countB = %d, countC = %d\n", countA, countB, countC);
        
        // This is the only case where we cannot satisfy the requirement,
        // since otherwise we can always use the entire string to satisify.
        if (countA < k || countB < k || countC < k) return -1;

        // The problem is equivalent to finding the longest subarray with at most
        // (countA - k, countB - k, countC - k) of ('a', 'b', 'c')
        int lsa = 0;  // Longest subarray
        int i = 0, j = 0;
        int ca = 0;
        int cb = 0;
        int cc = 0;
        char ch;
        while (j < s.length()) {
            ch = s.charAt(j);
            if (ch == 'a') {
                ca++;
            } else if (ch == 'b') {
                cb++;
            } else {
                cc++;
            }
            if (ca <= countA-k && cb <= countB-k && cc <= countC-k) {
                lsa = Math.max(lsa, j-i+1);
            } else {
                if (s.charAt(i) == 'a') {
                    ca--;
                } else if (s.charAt(i) == 'b') {
                    cb--;
                } else {
                    cc--;
                }
               i++; 
            }
            j++;
            // System.out.printf("i = %d, j = %d, %d, %d, %d\n", i, j, ca, cb, cc);
        }
        return s.length() - lsa;
    }
}
