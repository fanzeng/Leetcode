class Solution {
    public char findKthBit(int n, int k) {
        StringBuilder sb = new StringBuilder("0");
        for (int i = 0; i < n; i++) {
            grow(sb);
            // System.out.println(sb.toString());
            if (sb.length() >= k) {
                return sb.charAt(k-1);
            }
        }
        return '0';
    }
    void grow(StringBuilder sb) {
        StringBuilder sb2 = new StringBuilder();
        for (int i = sb.length() - 1; i > -1; i--) {
            if (sb.charAt(i) == '0') {
                sb2.append("1");
            } else {
                sb2.append("0");
            }
        }
        String s = sb2.toString();
        sb.append("1");
        sb.append(s);
    }
}
