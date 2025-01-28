class Solution {
    public int findMaxFish(int[][] grid) {
        int ans = 0;
        int[][] visited = new int[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int fish = 0;
                if (visited[i][j] == 0) {
                    fish = dfs(grid, i, j, visited);
                    if (fish > ans) ans = fish;
                }
            }
        }
        return ans;
    }
    private int dfs(int[][] grid, int r, int c, int[][] visited) {
        if (visited[r][c] == 1) return 0;
        visited[r][c] = 1;
        int fish = grid[r][c];
        if (fish == 0) return 0;
        if (r-1 >= 0) fish += dfs(grid, r-1, c, visited);
        if (c-1 >= 0) fish += dfs(grid, r, c-1, visited);
        if (r+1 < grid.length) fish += dfs(grid, r+1, c, visited);
        if (c+1 < grid[0].length) fish += dfs(grid, r, c+1, visited);
        return fish;
    }
}
