class Solution {
    public boolean canSortArray(int[] nums) {
        int psb = setBits(nums[0]); // Stores the set bits of the previous number
        int thisMax = nums[0];
        int thisMin = nums[0];
        List<Integer> segmentMax = new ArrayList<>();
        List<Integer> segmentMin = new ArrayList<>();
        for (int i = 1; i < nums.length; i++) {
            int sb = setBits(nums[i]);
            if (sb != psb) {
                psb = sb;
                segmentMax.add(thisMax);
                segmentMin.add(thisMin);
                thisMax = nums[i];
                thisMin = nums[i];
            }
            thisMax = Math.max(thisMax, nums[i]);
            thisMin = Math.min(thisMin, nums[i]);
        }
        segmentMax.add(thisMax);
        segmentMin.add(thisMin);
        for (int i = 1; i < segmentMax.size(); i++) {
            if (segmentMin.get(i) < segmentMax.get(i-1)) return false;
        }
        return true;
    }
    private int setBits(int num) {
        return Integer.bitCount(num);
    }
}
