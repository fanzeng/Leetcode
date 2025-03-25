class Solution {
    public boolean checkValidCuts(int n, int[][] rectangles) {
        int[][] x = new int[rectangles.length][2];
        int[][] y = new int[rectangles.length][2];
        for (int i = 0; i < rectangles.length; i++) {
            x[i][0] = rectangles[i][0];
            x[i][1] = rectangles[i][2];
            y[i][0] = rectangles[i][1];
            y[i][1] = rectangles[i][3];
        }
        return canCut(x) || canCut(y);
    }
    private boolean canCut(int[][] x) {
        if (x.length < 3) return false;
        Arrays.sort(x, (a, b) -> Integer.compare(a[0], b[0]));
        int end = x[0][1];
        int i = 0;
        int count = 0;
        while (++i < x.length) {
            int start = x[i][0];
            if (start >= end) {
                // System.out.printf("Cut No.%d at %d\n", count+1, end);
                count++;
                if (count == 2) break;
            }
            end = Math.max(end, x[i][1]);
        }
        if (count == 2 && i < x.length) return true;
        return false;
    }
}
