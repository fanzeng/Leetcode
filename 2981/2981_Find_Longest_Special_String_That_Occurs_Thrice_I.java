class Solution {
    public int maximumLength(String s) {
        if (!exists(s, 1)) return -1;
        return binarySearch(s, 1, 49);
    }
    private int binarySearch(String s, int l, int r) {
        while (l < r) {
            int m = (l + r) / 2;
            if (exists(s, m)) {
                l = m+1;
            } else {
                r = m;
            }
        }
        return l-1;
    }
    private boolean exists(String s, int m) {
        HashMap<String, Integer> h = new HashMap<>();
        for (int i = 0; i < s.length() - m + 1; i++) {
            String sub = s.substring(i, i+m);
            boolean dq = false;
            for (int j = 1; j < sub.length(); j++) {
                if (sub.charAt(j) != sub.charAt(j-1)) {
                    dq = true;
                    break;
                }
            }
            if (dq) continue;
            // System.out.println(sub);
            h.put(sub, h.getOrDefault(sub, 0) + 1);
            if (h.get(sub) == 3) return true;
        }
        return false;
    }
}
