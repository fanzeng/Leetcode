class Solution {
    public long minimumTotalDistance(List<Integer> robot, int[][] factory) {
        Collections.sort(robot);
        Arrays.sort(factory, Comparator.comparingInt(f -> f[0]));
        List<Integer> factories = new ArrayList<>(); // Locations of all factories from left to right.
        // Replace each factory with capacity k with k copies of factory with capacity 1.
        for (int[] f : factory) {
            for (int i = 0; i < f[1]; i++) {
                factories.add(f[0]);
            }
        }
        long[][] memo = new long[robot.size()][factories.size()];
        for (int i = 0; i < robot.size(); i++) {
            for (int j = 0; j < factories.size(); j++) {
                memo[i][j] = -1;
            }
        }
        return assign(0, 0, robot, factories, memo);
    }
    private long assign(int rId, int fId, List<Integer> robot, List<Integer> factories, long[][]memo) {
        // Edge conditions
        if (rId >= robot.size()) return 0; // All robots assigned, job done.
        if (fId >= factories.size()) return Long.MAX_VALUE/100; // Cannot arrange, return inf.

        // Check memo
        if (memo[rId][fId] >= 0) return memo[rId][fId];
        
        // Go through the robots from left to right,
        // For each robot, we either assign it to the next factory, or we don't,
        // there are only these two possibilities.
        // Also note it's a dominated strategy if any robot-factory pair crosses over, 
        // because we can always swap the assignment and (potentially) reduce the loss,
        // while keeping the capacity consumption unchanged (each robot consumes 1 factory).
        // Hence we can always ignore the possibility of a "later" robot gets assigned to an "eariler" factory.

        // Assign:
        long resAssign = Math.abs(robot.get(rId) - factories.get(fId)) + assign(rId+1, fId+1, robot, factories, memo);
        // Not assign:
        long resNotAssign = assign(rId, fId+1, robot, factories, memo);
        long res = Math.min(resAssign, resNotAssign);
        memo[rId][fId] = res;
        return res;
    }
}
