class Solution {
    public String longestDiverseString(int a, int b, int c) {
        StringBuilder sb = new StringBuilder("");
        while (a + b + c > 0) {
            boolean noProgress = true;
            if (a > 0) {
                var success = insert(sb, 'a');
                if (success) {
                    a--;
                    noProgress = false;
                }
            }
            if (b > 0) {
                var success = insert(sb, 'b');
                if (success) {
                    b--;
                    noProgress = false;
                }
            }
            if (c > 0) {
                var success = insert(sb, 'c');
                if (success) {
                    c--;
                    noProgress = false;
                }
            }
            // System.out.printf("a = %d, b = %d, c = %d\n", a, b, c);
            // System.out.printf("sb = %s\n", sb.toString());
            if (noProgress) break;
        }
        return sb.toString();
    }
    boolean insert(StringBuilder sb, char c) {
        int i = 0;
        if (sb.length() < 2) {
            sb.insert(0, c);
            return true;
        }
        if (sb.length() == 2) {
            if (sb.charAt(0) != c || sb.charAt(1) != c) {
                sb.insert(0, c);
                return true;
            } else {
                return false;
            }
        }
        while (i < sb.length()) {
            if (i > 1 && sb.charAt(i-2) == c && sb.charAt(i-1) == c) {
                i++;
                continue;
            }
            if (i > 0 && sb.charAt(i-1) == c && sb.charAt(i) == c) {
                i++;
                continue;
            }
            if (sb.charAt(i) != c || i + 1 == sb.length() || sb.charAt(i+1) != c) {
                sb.insert(i, c);
                return true;
            }
            i++;
        }
        if (sb.charAt(i-2) != c || sb.charAt(i-1) != c) {
            sb.append(c);
            return true;
        }
        return false;
    }
}
