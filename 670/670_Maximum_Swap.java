class Solution {
    public int maximumSwap(int num) {
        String s = String.format("%s", num);
        // System.out.printf("s = %s", s);
        char[] c = s.toCharArray();
        for (int i = 0; i < c.length; i++) {
            int d1 = (int)c[i];
            int currMax = 0;
            int currArgMax = -1;
            for (int j = i + 1; j < c.length; j++) {
                int d2 = (int)c[j];
                if (d2 <= d1) continue;
                if (d2 >= currMax) {
                    currMax = d2;
                    currArgMax = j;
                }
            }
            if (currMax > 0) {
                c[currArgMax] = (char)d1;
                c[i] = (char)currMax;
                break;
            }
        }
        return Integer.parseInt(new String(c));
    }
}
