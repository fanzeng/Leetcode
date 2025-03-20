class Solution {
    public int minCapability(int[] nums, int k) {
        int n = nums.length;
        int[][] dp = new int[3][k + 1];
        for (int i = 0; i < 3; i++) {
            dp[i][0] = 0;
            for (int j = 1; j <= k; j++) {
                dp[i][j] = -2; // Init unprocessed to -2
            }
        }
        dp[2][1] = nums[n - 1];
        if (n > 1) {
            dp[1][1] = Math.min(nums[n - 1], nums[n - 2]);
            if (k > 1)
                dp[1][2] = -1;
        }
        // Process infeasible i. If fewer houses to rob than required, it's infeasible.
        for (int j = 1; j <= k; j++) {
            for (int i = n - 1; i > n - j; i--) {
                dp[i % 3][j] = -1; // -1 for infeasible.
            }
        }
        // for (int i = 2; i > 0; i--) {
        // System.out.printf("%d: ", i%3);
        // for (int j = 1; j < dp[i].length; j++) {
        // System.out.print(dp[i][j] + " ");
        // }
        // System.out.println();
        // }

        // From nums[i:], steal j houses
        int r = 3 - (n % 3);
        for (int i = n - 3; i > -1; i--) {
            // System.out.printf("%d: ", (i+r)%3);
            for (int j = 1; j <= k; j++) {
                // if (dp[(i+0) % 3][j] == -1) continue;
                int stealI = Integer.MAX_VALUE, notStealI = Integer.MAX_VALUE;
                if (dp[(i + r + 2) % 3][j - 1] > -1) {
                    stealI = Math.max(nums[i], dp[(i + r + 2) % 3][j - 1]);
                }
                if (dp[(i + r + 1) % 3][j] > -1) {
                    notStealI = dp[(i + r + 1) % 3][j];
                }
                if (dp[(i + r + 2) % 3][j - 1] == -1 && dp[(i + r + 1) % 3][j] == -1) {
                    dp[(i + r + 0) % 3][j] = -1;
                } else {
                    dp[(i + r + 0) % 3][j] = Math.min(stealI, notStealI);
                }
                // System.out.print(dp[(i+r+0) % 3][j] + " ");
            }
            // System.out.println();
        }
        // for (int i = 0; i < dp.length; i++) {
        // for (int j = 0; j < dp[i].length; j++) {
        // System.out.print(dp[i][j] + " ");
        // }
        // System.out.println();
        // }
        return dp[r % 3][k];
    }
}
