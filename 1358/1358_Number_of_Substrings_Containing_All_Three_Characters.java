class Solution {
    public int numberOfSubstrings(String s) {
        int n = s.length();
        int pa = -1, pb = -1, pc = -1, p = -1;
        while (++p < n && (pa == -1 || pb == -1 || pc == -1)) {
            if (pa == -1 && s.charAt(p) == 'a') pa = p;
            if (pb == -1 && s.charAt(p) == 'b') pb = p;
            if (pc == -1 && s.charAt(p) == 'c') pc = p;
        }
        // System.out.printf("pa = %d, pb = %d, pc = %d\n", pa, pb, pc);
        if (pa == -1 || pb == -1 || pc == -1) return 0;
        p = Math.max(Math.max(pa, pb), pc);
        int res = n - p;
        int i = -1;
        while (++i < n) {
            char ch = s.charAt(i);
            if (ch == 'a' && pa == i) {
                while (++pa < n && s.charAt(pa) != 'a');
                if (pa == n) break;
            }
            if (ch == 'b' && pb == i) {
                while (++pb < n && s.charAt(pb) != 'b');
                if (pb == n) break;
            }
            if (ch == 'c' && pc == i) {
                while (++pc < n && s.charAt(pc) != 'c');
                if (pc == n) break;
            }
            p = Math.max(Math.max(pa, pb), pc);
            // System.out.printf("pa = %d, pb = %d, pc = %d, p = %d\n", pa, pb, pc, p);
            res += n - p;
        }
        return res;
    }
}
