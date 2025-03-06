class Solution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {
        int[] res = new int[2];
        int n = grid.length;
        Set<Integer> m = new HashSet<>();
        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                int k = grid[i][j];
                if (m.contains(k))  {
                    res[0] = k;
                } else {
                    m.add(k);
                    sum += k;
                }
            }
        }
        int s = n*n;
        int expected = s*(s+1)/2;
        res[1] = expected - sum;
        return res;
    }
}
