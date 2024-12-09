class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        // Sort the queries according to start index.
        int[][] orig = new int[queries.length][];
        for (int i = 0; i < queries.length; i++) {
            orig[i] = queries[i].clone();
        }
        HashMap<Integer, Boolean> memo = new HashMap<>();
        Arrays.sort(queries, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        // for (int[] q : queries) {
        //     System.out.println(Arrays.toString(q));
        // }
        boolean[] diff = new boolean[nums.length];
        for (int i = 0; i < nums.length-1; i++) {
            diff[i] = (nums[i]%2) != (nums[i+1]%2);
        }
        diff[nums.length-1] = true;
        int lastSame = -1;
        int latestGood = 0;
        for (int j = 0; j < queries.length; j++) {
            int[] q = queries[j];
            int from = q[0];
            int to = q[1];
            int h = hash(q[0], q[1]);
            if (from == to) {
                memo.put(h, true);
                continue;
            }
            if (from <= lastSame && to > lastSame) {
                memo.put(h, false);
                continue;
            }
            if (from > lastSame && to <= latestGood) {
                memo.put(h, true);
                continue;
            }
            memo.put(h, true);
            for (int k = Math.max(from, lastSame); k < to; k++) {
                if (!diff[k]) {
                    memo.put(h, false);
                    lastSame = k;
                    if (k > from) latestGood = k-1;
                    break;
                }
            }
            // If the last query we just checked is "good" (true),
            // then if next query is between lastSame and to, it should be "good" as well.
            if (memo.get(h)) latestGood = to;
        }
        boolean[] ans = new boolean[queries.length];
        for (int i = 0; i < orig.length; i++) {
            ans[i] = memo.get(hash(orig[i][0], orig[i][1]));
        }
        return ans;
    }
    private int hash(int i, int j) {
        return 100000*i + j;
    }
}
