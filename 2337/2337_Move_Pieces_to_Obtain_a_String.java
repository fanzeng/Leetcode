class Solution {
    public boolean canChange(String start, String target) {
        // L cannot go right past R and R cannot go left past L,
        // therefore the order of the pieces cannot change.
        // Match each piece in start to target.
        int i = 0, j = 0;
        while (true) {
            while (i < start.length() && start.charAt(i) == '_') i++;
            while (j < target.length() && target.charAt(j) == '_') j++;
            if (i < start.length() && j < target.length()) {
                if (start.charAt(i) != target.charAt(j)) return false;
                if (start.charAt(i) == 'L' && i < j) return false;
                if (start.charAt(i) == 'R' && i > j) return false;
            } else {
                return i == j;
            }
            i++; j++;
        }
    }
}
