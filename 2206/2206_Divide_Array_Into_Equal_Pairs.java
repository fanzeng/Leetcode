class Solution {
    public boolean divideArray(int[] nums) {
        int[] counts = new int[500];
        int sup = 0;
        for (int i = 0; i < nums.length; i++) {
            counts[nums[i]-1]++;
            if (nums[i] > sup) sup = nums[i];
        }
        for (int i = 0; i < sup; i++) {
            if (counts[i] % 2 == 1) return false;
        }
        return true;
    }
}
