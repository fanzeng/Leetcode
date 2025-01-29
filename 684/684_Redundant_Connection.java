class Solution {
    public int[] findRedundantConnection(int[][] edges) {
        int E = edges.length;
        List<Integer>[] adj = new ArrayList[E];
        for (int i = 0; i < E; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int i = 0; i < edges.length; i++) {
            int[] e = edges[i];
            int[] visited = new int[E];
            if (check(e[0]-1, e[1]-1, visited, adj)) {
                return new int[]{e[0], e[1]};
            }
            adj[e[0]-1].add(e[1]-1);
            adj[e[1]-1].add(e[0]-1);
        }
        return new int[]{};
    }
    private boolean check(int s, int t, int[] visited, List<Integer>[] adj) {
        if (s == t) return true;
        visited[s] = 1;
        for (int e : adj[s]) {
            if (visited[e] == 0) {
                if (check(e, t, visited, adj)) return true;
            }
        }
        return false;
    }
}
