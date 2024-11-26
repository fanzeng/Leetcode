class Solution {
    public int findChampion(int n, int[][] edges) {
        int[] weak = new int[n];
        for (int i = 0; i < edges.length; i++) {
            int[] e = edges[i];
            weak[e[1]] = 1;
        }
        int count = 0;
        int strong = -1;
        for (int i = 0; i < n; i++) {
            if (weak[i] == 0) {
                count++;
                if (count > 1) return -1;
                strong = i;
            }
        }
        return strong;
    }
}
