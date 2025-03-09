class Solution {
    public int numberOfAlternatingGroups(int[] colors, int k) {
        int res = 0;
        int n = colors.length;
        int i = 0, j = 0;
        while (i < n) {
            j++;
            if (colors[j % n] == colors[(j-1) % n]) {
                i++; j = i;
                continue;
            }
            if (j-i+1 == k) {
                while (colors[j % n] != colors[(j-1) % n] && i < n) {
                    res++; i++; j++;
                }
                j = i;
            }
        }
        return res;
    }
}
