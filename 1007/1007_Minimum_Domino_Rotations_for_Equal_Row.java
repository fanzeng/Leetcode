class Solution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        int rtt = rotate(tops, bottoms, tops[0]);
        int rtb = rotate(tops, bottoms, bottoms[0]);
        int rbt = rotate(bottoms, tops, tops[0]);
        int rbb = rotate(bottoms, tops, bottoms[0]);
        int[] res = {rtt, rtb, rbt, rbb};
        if (Arrays.stream(res).sum() == -4) return -1;
        return Arrays.stream(res).filter(r -> r >= 0).min().orElse(Integer.MAX_VALUE);
    }
    private int rotate(int[] a0, int[] a1, int target) {
        int count = 0;
        for (int i = 0; i < a0.length; i++) {
            if (a0[i] == target) continue;
            if (a1[i] != target) return -1;
            count++;
        }
        return count;
    }
}
