class Solution {
    public int maxUniqueSplit(String s) {
        Set<String> set = new HashSet<>();
        return dp(s, set);
    }
    int dp(String s, Set<String> set) {
        int ans = -1;
        for (int i = 0; i < s.length()-1; i++) {
            String sub1 = s.substring(0, i+1);
            if (set.contains(sub1)) {
                continue;
            }
            String sub2 = s.substring(i+1);
            set.add(sub1);
            int res = dp(sub2, set);
            set.remove(sub1);
            if (res < 0) continue;
            res += 1;
            if (res > ans) {
                ans = res;
            }
        }
        if (ans > 0) return ans;
        if (set.contains(s)) return -1;
        return 1;
    }
}
