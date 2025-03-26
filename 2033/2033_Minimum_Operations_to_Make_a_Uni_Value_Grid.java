class Solution {
    public int minOperations(int[][] grid, int x) {
        int n = grid.length*grid[0].length;
        if (n == 1) return 0;
        int[] arr = new int[n];
        int k = 0;
        int r = grid[0][0] % x;
        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                arr[k++] = grid[i][j];
                if (grid[i][j] % x != r) return -1;
                sum += grid[i][j];
            }
        }
        Arrays.sort(arr);
        int res = getNumberOfOps(arr, arr[n/2], x);
        if (n % 2 == 0) return res;
        res = Math.min(res, getNumberOfOps(arr, arr[n/2+1], x));
        return res;
    }
    private int getNumberOfOps(int[] arr, int m, int x) {
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            count += Math.abs(arr[i] - m) / x;
        }
        return count;
    }
}
