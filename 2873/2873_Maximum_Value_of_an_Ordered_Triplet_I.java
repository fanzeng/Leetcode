class Solution {
    public long maximumTripletValue(int[] nums) {
        long res = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                for (int k = j+1; k < nums.length; k++) {
                    if (nums[i] < 0 && nums[j] < 0 && nums[k] < 0) continue;
                    res = Math.max(res, (nums[i] - nums[j])*(long)nums[k]);
                }
            }
        }
        return res;
    }
}
