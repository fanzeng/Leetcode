class Solution {
    public int maxMoves(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] res = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = -1;
            }
        }
        res[m-1][n-1] = 0;
        int ans = -1;
        for (int i = 0; i < m; i++) {
            res[i][0] = dp(i, 0, grid, res);
            // System.out.println(res[i][0]);
            if (res[i][0] > ans) ans = res[i][0];
        }
        return ans;
    }
    public int dp(int r, int c, int[][] grid, int[][] res) {
        int curr = grid[r][c];
        int ans = 0;
        if (res[r][c] >= 0) return res[r][c];
        if (r > 0 && c < grid[0].length-1 && grid[r-1][c+1] > curr) ans = Math.max(ans, 1 + dp(r-1, c+1, grid, res));
        if (c < grid[0].length-1 && grid[r][c+1] > curr) ans = Math.max(ans, 1 + dp(r, c+1, grid, res));
        if (r < grid.length-1 && c < grid[0].length-1 && grid[r+1][c+1] > curr) ans = Math.max(ans, 1 + dp(r+1, c+1, grid, res));
        res[r][c] = ans;
        // System.out.printf("%d, %d, %d\n", r, c, ans);
        return ans;
    }
}
