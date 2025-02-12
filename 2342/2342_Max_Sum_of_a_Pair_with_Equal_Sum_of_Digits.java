class Solution {
    public int maximumSum(int[] nums) {
        HashMap<Integer, int[]> h = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int n = nums[i];
            int s = getSum(n);
            int[] arr = h.getOrDefault(s, new int[2]);
            int a = arr[0];
            int b = arr[1];
            arr = getLargestTwo(a, b, n);
            h.put(s, arr);
        }
        int ans = -1;
        for (Map.Entry<Integer, int[]> e : h.entrySet()) {
            int[] arr = e.getValue();
            if (arr[1] == 0) continue;
            int s = arr[0] + arr[1];
            if (s > ans) ans = s;
        }
        return ans;
    }
    private int getSum(int n) {
        int s = 0;
        char[] chArr = Integer.toString(n).toCharArray();
        for (int i = 0; i < chArr.length; i++) {
            s += Character.getNumericValue(chArr[i]);
        }
        return s;
    }
    private static int[] getLargestTwo(int a, int b, int c) {
        int largest, secondLargest;
        if (a > b) {
            if (a > c) {
                largest = a;
                secondLargest = Math.max(b, c);
            } else {
                largest = c;
                secondLargest = a;
            }
        } else {
            if (b > c) {
                largest = b;
                secondLargest = Math.max(a, c);
            } else {
                largest = c;
                secondLargest = b;
            }
        }
        return new int[]{largest, secondLargest};
    }
}
