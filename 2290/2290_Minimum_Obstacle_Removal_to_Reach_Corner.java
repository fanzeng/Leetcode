class Solution {
    public int minimumObstacles(int[][] grid) {
        return dijkstra(grid);
    }
    class Point {
        private int r;
        private int c;
        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
        public List<Point> adj(int h, int w) {
            List<Point> a = new ArrayList<>();
            if (r > 0) a.add(new Point(r-1, c));
            if (r+1 < h) a.add(new Point(r+1, c));
            if (c > 0) a.add(new Point(r, c-1));
            if (c+1 < w) a.add(new Point(r, c+1));
            return a;
        }
    }
    private int dijkstra(int[][] grid) {
        int h = grid.length;
        int w = grid[0].length;
        Point s = new Point(0, 0);
        Point t = new Point(h-1, w-1);
        if (s == t) return 0;
        LinkedList<Point> q = new LinkedList<>();
        int[][] visited = new int[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                visited[i][j] = -1;
            }
        }
        q.add(s);
        visited[s.r][s.c] = 0;
        while(q.size() > 0) {
            Point v = q.poll();
            int dist = visited[v.r][v.c];
            List<Point> a = v.adj(h, w);
            for (int i = 0; i < a.size(); i++) {
                Point u = a.get(i);
                if (u == t) return dist;
                int d = visited[u.r][u.c];
                int dg = dist + grid[v.r][v.c];
                if (d < 0 || d > dg) {
                    visited[u.r][u.c] = dg;
                    q.add(u);
                }
            }
            // printVisited(visited);
        }
        return visited[t.r][t.c];
    }
    private void printVisited(int[][] visited) {
        for (int i = 0; i < visited.length; i++) {
            for (int j = 0; j < visited[0].length; j++) {
                System.out.printf("%d,", visited[i][j]);
            }
            System.out.println();
        }
        System.out.println();
    }
}
