class Solution {
    public int countUnguarded(int m, int n, int[][] guards, int[][] walls) {
        int[][] tiles = new int[m][n];
        for (int w = 0; w < walls.length; w++) {
            tiles[walls[w][0]][walls[w][1]] = -1;
        } 
        for (int g = 0; g < guards.length; g++) {
            tiles[guards[g][0]][guards[g][1]] = -2;
        }
        for (int g = 0; g < guards.length; g++) {
            guard(tiles, guards[g][0], guards[g][1]);
        } 
        // printTiles(tiles);
        int sum = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (tiles[i][j] == 0) sum += 1;
            }
        }
        return sum;
    }
    private void guard(int[][] tiles, int y, int x) {
        int l = x-1;
        while(l > -1) {
            if (tiles[y][l] < 0) break;
            tiles[y][l] = 1;
            l--;
        }
        int r = x+1;
        while(r < tiles[0].length) {
            if (tiles[y][r] < 0) break;
            tiles[y][r] = 1;
            r++;
        }
        int u = y-1;
        while(u > -1) {
            if (tiles[u][x] < 0) break;
            tiles[u][x] = 1;
            u--;
        }
        int d = y+1;
        while(d < tiles.length) {
            if (tiles[d][x] < 0) break;
            tiles[d][x] = 1;
            d++;
        }
    } 
    private void printTiles(int[][] tiles) {
        for (int i = 0; i < tiles.length; i++) {
            for (int j = 0; j < tiles[0].length; j++) {
                switch (tiles[i][j]) {
                    case 0:
                        System.out.printf("O ");
                        break;
                    case -1:
                        System.out.printf("W ");
                        break;
                    default:
                        System.out.printf("G ");
                }
            }
            System.out.println();
        }

    }
}
