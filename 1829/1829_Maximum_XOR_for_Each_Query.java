class Solution {
    public int[] getMaximumXor(int[] nums, int maximumBit) {
        int[] xors = new int[nums.length];
        int[] ans = new int[nums.length];
        xors[0] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            xors[i] = xors[i-1] ^ nums[i];
        }
        for (int i = 0; i < nums.length; i++) {
            ans[i] = getMaxXor(xors[nums.length - 1 - i], maximumBit);
        }
        return ans;
    }
    private int getMaxXor(int n, int b) {
        int allOnes = (1 << b) - 1;
        int k = allOnes ^ (allOnes & n);
        // System.out.printf("n = %d, b = %d, allOnes = %d, k = %d\n", n, b, allOnes, k);
        return k;
    }
}
