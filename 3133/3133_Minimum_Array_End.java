class Solution {
    public long minEnd(int n, int x) {
        // For the bitwise AND to be x,
        // all 1 bits in x must be 1 for every num,
        // and the 0 bits must have at least 1 zero.
        String xb = Integer.toBinaryString(x);
        // System.out.printf("xb = %s\n", xb);
        String n1b = Integer.toBinaryString(n-1);
        // System.out.printf("n1b = %s\n", n1b);
        int count = 0;
        int i = xb.length() - 1;
        int j = n1b.length() - 1;
        long res = 0;
        long b = 1;
        while (i >= 0 || j >= 0) {
            // System.out.printf("i = %d, j = %d\n", i, j);
            if (i >= 0 && xb.charAt(i) == '1') {
                res += b;
            } else if (j >= 0) {
                if (n1b.charAt(j) == '1') res += b;
                j--;
            }
            if (i >= 0) i--;
            b *= 2;
        }
        return res;
    }
}
