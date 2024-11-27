class Solution {
    public int[] shortestDistanceAfterQueries(int n, int[][] queries) {
        int[] memo = new int[n];  // Min. dist to last node
        List<Integer>[] adj = new List[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < n-1; i++) {
            adj[i].add(i+1);
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            resetMemo(memo);
            int[] road = queries[i];
            int rs = road[0];
            int rt = road[1];
            adj[rs].add(rt);
            dp(0, adj, memo);
            ans[i] = memo[0];
            // System.out.printf("i = %d\n", i);
            // printMemo("memo", memo);
            // printAdj("adj", adj);
        }
        return ans;
    }
    private int dp(int s, List<Integer>[] adj, int[] memo) {
        if (memo[s] >= 0) return memo[s];
        int minDist = memo.length;
        for (int i = 0; i < adj[s].size(); i++) {
            int next = adj[s].get(i);
            int dist = 1 + dp(next, adj, memo);
            if (dist < minDist) minDist = dist;
        }
        memo[s] = minDist;
        return minDist;
    }
    private void resetMemo(int[] memo) {
        for (int i = 0; i < memo.length-1; i++) {
            memo[i] = -1;
        }
        memo[memo.length-1] = 0;
    }
    private void printMemo(String label, int[] memo) {
        System.out.printf("%s: [", label);
        for (int i = 0; i < memo.length; i++) {
            System.out.printf("%d,", memo[i]);
        }
        System.out.println("]");
    }
    private void printAdj(String label, List<Integer>[] adj) {
        System.out.printf("%s:\n", label);
        for (int i = 0; i < adj.length; i++) {
            System.out.printf("%d:", i);
            for (int j = 0; j < adj[i].size(); j++) {
                System.out.printf("%d,", adj[i].get(j));
            }
            System.out.println();
        }
    }
}
