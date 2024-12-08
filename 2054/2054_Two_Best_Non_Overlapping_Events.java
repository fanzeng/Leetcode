class Solution {
    public int maxTwoEvents(int[][] events) {
        Arrays.sort(events, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        for (int[] event: events) {
            // System.out.println(Arrays.toString(event));
        }
        int[] dp = new int[events.length];
        dp[events.length-1] = events[events.length-1][2];
        int res = events[events.length-1][2];
        for (int i = events.length-2; i > -1; i--) {
            int[] e = events[i];
            int attend;
            int j = binarySearch(events, i+1, events.length, e[1]);
            while (j < events.length && events[j][0] <= e[1]) j++;
            if (j == events.length) {
                attend = e[2];
            } else {
                attend = e[2] + dp[j];
            }
            res = Math.max(res, attend);
            dp[i] = Math.max(e[2], dp[i+1]);
        }
        // System.out.println("dp = " + Arrays.toString(dp));
        return res;
    }
    // Find first index of events with start time > v
    private int binarySearch(int[][] events, int l, int r, int v) {
        while (l < r) {
            int m = (l + r) / 2;
            if (events[m][0] > v) {
                r = m;
            } else {
                l = m+1;
            }
        }
        return l;
    }
}
