class Solution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int m = str1.length();
        int n = str2.length();
        String[][] dp = new String[2][n + 1];

        for (int j = 0; j <= n; j++) {
            dp[0][j] = str2.substring(0, j);
        }
        for (int i = 1; i <= m; i++) {
            dp[i % 2][0] = str1.substring(0, i);
            for (int j = 1; j <= n; j++) {
                if (str1.charAt(i - 1) == str2.charAt(j - 1)) {
                    dp[i % 2][j] = dp[(i - 1) % 2][j - 1] + str1.charAt(i - 1);
                } else {
                    String r1 = dp[(i - 1) % 2][j];
                    String r2 = dp[i % 2][j - 1];
                    dp[i % 2][j] = r1.length() < r2.length() ? r1 + str1.charAt(i - 1) : r2 + str2.charAt(j - 1);
                }
            }
        }
        return dp[m % 2][n];
    }
}
