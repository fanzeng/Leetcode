class Solution {
    public boolean checkPowersOfThree(int n) {
        int[] p3 = new int[17];
        for (int i = 0; i < p3.length; i++) {
            p3[i] = (int) Math.pow(3, 16-i);
            // System.out.printf("3^%d = %d\n", 16-i, p3[i]);
        }
        return check(n, p3, 0);
    }
    private boolean check(int n, int[] p3, int i) {
        // System.out.printf("n = %d, i = %d, p3[i] = %d\n", n, i, p3[i]);
        if (n < 0) return false;
        if (n == 0) return true;
        if (++i >= p3.length) return false;
        boolean notUse = check(n, p3, i);
        boolean use = check(n - p3[i], p3, i);
        return notUse || use;
    }
}
