class Solution {
    public int[] minOperations(String boxes) {
        int[] left = new int[boxes.length()];
        int[] right = new int[boxes.length()];
        int sum = 0; // Running sum to the left
        int moves = 0;
        for (int i = 0; i < boxes.length(); i++) {
            moves += sum;
            left[i] = moves;
            sum += boxes.charAt(i) - '0';
        }
        // System.out.println("left = " + Arrays.toString(left));
        sum = 0;
        moves = 0;
        for (int i = boxes.length() - 1; i > -1; i--) {
            moves += sum;
            right[i] = moves;
            sum += boxes.charAt(i) - '0';
        }
        // System.out.println("right = " + Arrays.toString(right));
        int[] ans = new int[boxes.length()];
        for (int i = 0; i < boxes.length(); i++) {
            ans[i] = left[i] + right[i];
        }
        return ans;
    }
}
