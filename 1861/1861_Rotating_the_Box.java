class Solution {
    public char[][] rotateTheBox(char[][] box) {
        char[][] ans = new char[box[0].length][box.length];
        for (int i = 0; i < box.length; i++) {
            char[] row = box[i];
            rotate(row, ans, box.length-i-1);
        }
        return ans;
    }
    private void rotate(char[] row, char[][]ans, int col) {
        int start = 0;
        int count = 0;
        for (int i = 0; i < row.length; i++) {
            if (row[i] == '*') {
                populate(ans, col, start, i, count);
                ans[i][col] = '*';
                start = i+1;
                count = 0;
            } else {
                if (row[i] == '#') count++;
            }
        }
        populate(ans, col, start, row.length, count);
    }
    private void populate(char[][] ans, int col, int start, int end, int count) {
        for (int i = end-1; i >= start; i--) {
            if (count > 0) {
                ans[i][col] = '#';
                count--;
            } else {
                ans[i][col] = '.';
            }
        }
    }
}
