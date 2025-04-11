class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i <= high; i++) {
            char[] chars = String.valueOf(i).toCharArray();
            int s1 = 0, s2 = 0;
            if (chars.length % 2 == 1) continue;
            for (int j = 0; j < chars.length / 2; j++) {
                s1 += chars[j] - '0';
            }
            for (int j = chars.length / 2; j < chars.length; j++) {
                s2 += chars[j] - '0';
            }
            if (s1 == s2) count++;
        }
        return count;
    }
}
