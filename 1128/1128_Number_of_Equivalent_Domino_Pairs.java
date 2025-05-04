class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] counts = new int[81];
        for (int i = 0; i < dominoes.length; i++) {
            int a = dominoes[i][0]-1;
            int b = dominoes[i][1]-1;
            counts[Math.max(a, b)*9 + Math.min(a, b)]++;
        }
        int res = 0;
        for (int i = 0; i < 81; i++) {
            // System.out.printf("counts[%d] = %d\n", i, counts[i]);
            if (counts[i] > 0) {
                res += counts[i]*(counts[i]-1)/2;
            }
        }
        return res;
    }
}
