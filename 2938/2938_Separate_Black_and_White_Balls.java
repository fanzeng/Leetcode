class Solution {
    public long minimumSteps(String s) {
        if (s.length() < 2) return 0;
        int countB = 0, countW = 0;
        for (char c : s.toCharArray()) {
            if (c == '0') countW++;
            if (c == '1') countB++;
        }
        // System.out.printf("countW = %d, countB = %d\n", countW, countB);
        long res = 0;
        int i = countW-1;
        int j = s.length()-1;
        while (true) {
            // Find the next black ball on the "white" segment
            while (i >= 0 && s.charAt(i) == '0') {
                i--;
            }
            // Find the next white ball on the "black" segment
            while (j >= 0 && s.charAt(j) == '1') {
                j--;
            }
            // System.out.printf("i = %d, j = %d\n", i, j);
            if (i < 0) {
                break;
            } else {
                res += j - i;
            }
            i--;
            j--;
        }
        return res;
    }
}
