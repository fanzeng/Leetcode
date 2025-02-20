class Solution {
    public String findDifferentBinaryString(String[] nums) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < nums.length; i++) {
            sb.append(Integer.toString(1 - Character.getNumericValue(nums[i].charAt(i))));
        }
        return sb.toString();
    }
}
