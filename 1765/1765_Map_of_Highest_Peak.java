class Solution {
    public int[][] highestPeak(int[][] isWater) {
        List<int[]> water = findWater(isWater);
        int[][] ans = new int[isWater.length][isWater[0].length];
        int[][] visited = new int[isWater.length][isWater[0].length];
        Queue<int[]> q = new LinkedList<>();
        for (int[] w : water) q.add(new int[]{w[0], w[1], 0});
        for (int[] w : water) visited[w[0]][w[1]] = 1;
        while (!q.isEmpty()) {
            int[] v = q.poll();
            // System.out.printf("[%d, %d] = %d\n", v[0], v[1], v[2]);
            ans[v[0]][v[1]] = v[2];
            List<int[]> neighbors = getNeighbors(v, ans.length, ans[0].length);
            for (int[] n : neighbors) {
                if (visited[n[0]][n[1]] == 0) {
                    q.add(new int[]{n[0], n[1], v[2]+1});
                    visited[n[0]][n[1]] = 1;
                }
            }
        }
        return ans;
    }
    private List<int[]> findWater(int[][] w) {
        List<int[]> water = new ArrayList<>();
        for (int i = 0; i < w.length; i++) {
            for (int j = 0; j < w[0].length; j++) {
                if (w[i][j] == 1) water.add(new int[]{i, j});
            }
        }
        return water;
    }
    private static List<int[]> getNeighbors(int[] point, int h, int w) {
        List<int[]> neighbors = new ArrayList<>();
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] dir : directions) {
            int r = point[0] + dir[0];
            int c = point[1] + dir[1];
            if (r < 0 || c < 0 || r == h || c == w) continue;
            int[] neighbor = new int[]{r, c};
            neighbors.add(neighbor);
        }
        return neighbors;
    }
}
