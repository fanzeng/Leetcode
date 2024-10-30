class Solution {
    public int minimumMountainRemovals(int[] nums) {
        int res = nums.length;
        for (int i = 1; i < nums.length-1; i++) {
            int curr = nums[i];
            int[] left = Arrays.stream(nums, 0, i)
                .filter(n -> n < curr)
                .toArray();
            if (left.length == 0) continue;
            int[] right = Arrays.stream(nums, i+1, nums.length)
                .filter(n -> n < curr)
                .boxed()
                .collect(Collectors.collectingAndThen(Collectors.toList(), list -> {
                    Collections.reverse(list);
                    return list.stream();
                }))
                .mapToInt(Integer::intValue)
                .toArray();
            if (right.length == 0) continue;
            int lisLeft = lis(left);
            int lisRight = lis(right);
            // System.out.printf("i = %d, left = %d, right = %d\n", i, lisLeft, lisRight);
            int ans = nums.length - (lisLeft + lisRight + 1);
            if (ans < res) res = ans;
        }
        return res;
    }
    private int lis(int[] nums) {
        int[] lis = new int[nums.length];
        lis[0] = nums[0];
        int length = 1;
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            if (n > lis[length-1]) {
                lis[length++] = n;
            } else {
                int j = binarySearch(lis, -1, length-1, n);
                lis[j] = n;
            }
        }
        return length;
    }
    private int binarySearch(int[] arr, int l, int r, int n) {
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (arr[m] >= n) {
                r = m;
            } else {
                l = m;
            }
        }
        return r;
    }
}
