class Solution {
    public int countSegments(String s) {
        if (s.length() == 0) {
            return 0;
        }
        if (s.length() == 1) {
            return s.charAt(0) != ' ' ? 1 : 0;
        }
        int count = 0;
        int j = 0;
        int k = s.length() - 1;
        while (j < s.length()-1 && s.charAt(j) == ' ') {
            j++;
        }
        while (k > 0 && s.charAt(k) == ' ') {
            k--;
        }
        if (k <= j) {
            return 0;
        }
        for (int i = j; i < k; i++) {
            if (s.charAt(i) == ' ' && i > 0 && s.charAt(i-1) != ' ') {
                count++;
            }
        }
        return count+1;
    }
}
