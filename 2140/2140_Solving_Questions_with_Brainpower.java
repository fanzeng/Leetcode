class Solution {
    public long mostPoints(int[][] questions) {
        long[] memo = new long[questions.length];
        Arrays.fill(memo, -1);
        return recurse(questions, 0, memo);
    }
    private long recurse(int[][] q, int i, long[] memo) {
        if (i >= q.length) return 0;
        if (i == q.length-1) return q[i][0];
        if (memo[i] != -1) return memo[i];
        long solve = q[i][0] + recurse(q, i+q[i][1]+1, memo);
        long notSolve = recurse(q, i+1, memo);
        long res = Math.max(solve, notSolve);
        memo[i] = res;
        return res;
    }
}
