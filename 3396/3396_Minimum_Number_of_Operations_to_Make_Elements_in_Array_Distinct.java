class Solution {
    public int minimumOperations(int[] nums) {
        int[] count = new int[101];
        int dup = 0;
        for (int i = 0; i < nums.length; i++) {
            count[nums[i]]++;
            if (count[nums[i]] == 2) dup++;
        }
        if (dup == 0) return 0;
        int res = 0;
        int i = 0;
        while (i < nums.length-1) {
            for (int j = 0; j < 3; j++) {
                count[nums[i]]--;
                if (count[nums[i++]] == 1) {
                    if (--dup == 0) return res+1;
                }
            }
            res++;
        }
        return res;
    }
}
