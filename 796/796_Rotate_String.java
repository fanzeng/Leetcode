class Solution {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;
        int len = goal.length();
        int i = 0;
        while (i < len) {
            int j = 0;
            int ii = i;
            int count = 0;
            while(s.charAt(ii) == goal.charAt(j)) {
                count++;
                ii++;
                j++;
                if (ii >= len) ii -= len;
                if (j >= len) j -= len;
                if (count == len) return true;
            }
            i++;
        }
        return false;
    }
}
