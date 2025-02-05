class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int count = 0;
        int diffIdx = -1;
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (count >= 2) return false;
                if (count == 0) {
                    diffIdx = i;
                    count++;
                } else {
                    if (s1.charAt(i) != s2.charAt(diffIdx) || s1.charAt(diffIdx) != s2.charAt(i)) {
                        return false;
                    }
                    count++;
                }
            }
        }
        return count == 0 || count == 2;
    }
}
