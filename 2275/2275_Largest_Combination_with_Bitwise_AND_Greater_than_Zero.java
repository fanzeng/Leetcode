class Solution {
    public int largestCombination(int[] candidates) {
        ArrayList<Integer>[] hasOne = new ArrayList[24];
        for (int b = 0; b < 24; b++) {
            hasOne[b] = new ArrayList<>();
        }
        for (int i = 0; i < candidates.length; i++) {
            int n = candidates[i];
            for (int b = 0; b < 24; b++) {
                int m = 1 << b;
                if ((n & m) > 0) {
                    hasOne[b].add(n);
                }
            }
        }
        int res = 0;
        for (int b = 0; b < 24; b++) {
            if (hasOne[b].size()> res) res = hasOne[b].size();
        }
        return res;
    }
}
