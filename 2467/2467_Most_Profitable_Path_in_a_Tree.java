class Solution {
    private Map<Integer, Integer> nodeToBobTime = new HashMap<>(); // Maps node to time that bob visit it.
    private List<List<Integer>> tree = new ArrayList<>();
    public int mostProfitablePath(int[][] edges, int bob, int[] amount) {
        for (int i = 0; i < amount.length; i++) {
            tree.add(new ArrayList<>());
        }
        for (int[] e : edges) {
            tree.get(e[0]).add(e[1]);
            tree.get(e[1]).add(e[0]);
        }
        bobMoves(bob, 0, new boolean[amount.length]);
        // Start BFS
        int maxScore = Integer.MIN_VALUE;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 0});
        boolean[] visited = new boolean[amount.length];
        while (!q.isEmpty()) {
            int[] n = q.poll();
            int s = n[0];
            int time = n[1];
            int score = n[2];
            // System.out.printf("s = %d\n", s);
            if (!nodeToBobTime.containsKey(s) || time < nodeToBobTime.get(s)) {
                score += amount[s];
            } else if (time == nodeToBobTime.get(s)) {
                score += amount[s]/2;
            }
            if (tree.get(s).size() == 1 && s != 0) {
                maxScore = Math.max(maxScore, score);
            } else {
                for (int adj : tree.get(s)) {
                    if (!visited[adj]) {
                        q.add(new int[]{adj, time+1, score});
                    }
                }
            }
            visited[s] = true;
        }
        return maxScore;
    }
    private boolean bobMoves(int s, int time, boolean[] visited) {
        nodeToBobTime.put(s, time);
        visited[s] = true;
        if (s == 0) return true;
        for (int adj : tree.get(s)) {
            if (!visited[adj]) {
                if (bobMoves(adj, time+1, visited)) return true;
            }
        }
        nodeToBobTime.remove(s);
        return false;
    }
}
