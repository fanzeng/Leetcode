class Solution {
    public int minimumTime(int[][] grid) {
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
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> Integer.compare(a[0], b[0]));
        int[][] visited = new int[h][w];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                visited[i][j] = -1;
            }
        }
        q.add(new int[]{0, s.r, s.c});
        visited[s.r][s.c] = 0;
        while(q.size() > 0) {
            int[] curr = q.poll();
            Point v = new Point(curr[1], curr[2]);
            int dist = visited[v.r][v.c];
            List<Point> a = v.adj(h, w);
            int blocked = 0;
            for (int i = 0; i < a.size(); i++) {
                Point u = a.get(i);
                if (u == t) return dist;
                int dg = dist+1;
                int du = grid[u.r][u.c];
                if (dg < du) {
                    blocked += 1;
                    if ((du - dg) % 2 == 0) {
                        dg = du;
                    } else {
                        dg = du + 1;
                    }
                }
                int d = visited[u.r][u.c];
                if (d < 0 || d > dg) {
                    visited[u.r][u.c] = dg;
                    q.add(new int[]{dg, u.r, u.c});
                }
            }
            // System.out.printf("%d, %d: blocked = %d\n", v.r, v.c, blocked);
            if (blocked == a.size()) return -1;
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
