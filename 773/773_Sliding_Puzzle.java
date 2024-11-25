class Solution {
    public int slidingPuzzle(int[][] board) {
        // Board b = new Board(board);
        // List<Board> neighbors = getNeighbors(b);
        // for (int i = 0; i < neighbors.size(); i++) {
        //     System.out.println(neighbors.get(i));
        // }
        Board t = new Board(new int[][]{{1,2,3}, {4,5,0}});
        return bfs(new Board(board), t);
    }
    private int bfs(Board b, Board t) {
        if (b.equals(t)) return 0;
        HashMap<Integer, Integer> visited = new HashMap<>();
        LinkedList<Board> q = new LinkedList<Board>();
        visited.put(b.hash(), 0);
        q.add(b);
        while (q.size() > 0) {
            Board v = q.poll();
            // System.out.println("v =\n" + v);
            int dist = visited.get(v.hash());
            List<Board> neighbors = getNeighbors(v);
            for (int i = 0; i < neighbors.size(); i++) {
                Board n = neighbors.get(i);
                // System.out.println(n);
                if (n.equals(t)) return dist+1;
                if (visited.get(n.hash()) == null) {
                    visited.put(n.hash(), dist+1);
                    q.add(n);
                }
            }
            // System.out.printf("q.size() = %d\n", q.size());
        }
        return -1;
    }
    class Board {
        int[][] arr;
        public Board(int h, int w) {
            arr = new int[h][w];
        }
        public Board(int[][] board) {
            arr = board;
        }
        public boolean equals(Board o) {
            return hash() == o.hash();
        }
        public int hash() {
            int hash = 0;
            int base = 1;
            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < arr[0].length; j++) {
                    hash += base*arr[i][j];
                    base *= 10;
                }
            }
            return hash;
        }
        public int[] getZero() {
            int r = -1, c = -1;
            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < arr[0].length; j++) {
                    if (arr[i][j] == 0) {
                        r = i; c = j; break;
                    }
                }
            }
            return new int[]{r, c};
        }
        public Board swap(int[] a, int[] b) {
            Board newBoard = new Board(arr.length, arr[0].length);
            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < arr[i].length; j++) {
                    newBoard.arr[i][j] = arr[i][j];
                }
            }
            int av = arr[a[0]][a[1]];
            int bv = arr[b[0]][b[1]];
            // System.out.printf("Swapping %d and %d\n", av, bv);
            newBoard.arr[a[0]][a[1]] = bv;
            newBoard.arr[b[0]][b[1]] = av;
            return newBoard;
        }
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < arr.length; i++) {
                for (int j = 0; j < arr[i].length; j++) {
                    sb.append(String.format("%d,\t", arr[i][j]));
                }
                sb.append("\n");
            }
            return sb.toString();
        }
    }
    private List<Board> getNeighbors(Board board) {
        List<Board> neighbors = new ArrayList<>();
        int h = board.arr.length;
        int w = board.arr[0].length;
        int[] zero = board.getZero();
        // System.out.printf("zero[0] = %d, zero[1] = %d\n", zero[0], zero[1]);
        for (int i = -1; i < 2; i += 2) {
            int r = zero[0] + i;
            if (r >= 0 && r < h) {
                Board neighbor = board.swap(zero, new int[]{r, zero[1]});
                neighbors.add(neighbor);
            }
        }
        for (int j = -1; j < 2; j += 2) {
            int c = zero[1] + j;
            if (c >= 0 && c < w) {
                Board neighbor = board.swap(zero, new int[]{zero[0], c});
                neighbors.add(neighbor);
            }
        }
        return neighbors;
    }
}
