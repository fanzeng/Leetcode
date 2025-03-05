class Solution {
    public long coloredCells(int n) {
        long size = 2*n - 1;
        return (size+1)*n - size;
    }
}
