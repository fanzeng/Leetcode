class Solution {
    public boolean canBeValid(String s, String locked) {
        if (s.length() % 2 == 1) return false;
        int lo = 0; // Locked open
        int u = 0; // Unlocked
        // 1st pass, left to right, make sure all locked ')' can be matched.
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(' && locked.charAt(i) == '1') { // Locked '('
                lo++;
            } else if (locked.charAt(i) == '0') { // Unlocked
                u++;
            } else { // Locked ')'
                if (lo > 0) {
                    lo--;
                } else if (u > 0) {
                    u--;
                } else {
                    return false;
                }
            }
        }
        // System.out.printf("lo = %d, u = %d\n", lo, u);
        // By now, we know all locked ')' can be matched,
        // and there are lo unmatched locked '(' remaining after matching all locked ')'.
        // These needs to be matched with u unlocked ones.
        // Since we consumed the unlocked from left to right,
        // we know the remaining unlocked ones are the rightmost ones.
        // We also know that the remaining locked '(' are the rightmost lo locked '(',
        // Because previously we've prioritised matching locked ')' with locked '(' first.
        int buffer = 0;
        // 2nd pass, right to left, match all locked '('.
        // Any unlocked char or locked ')' will match a locked '(', increasing the buffer.
        // A locked '(' will consume the buffer.
        // Any time buffer dips below 0, we have a locked '(' that cannot be possibly matched.
        for (int i = s.length()-1; i > -1; i--) {
            if (locked.charAt(i) == '0') {
                buffer++;
                u--;
            } else if (s.charAt(i) == '(') {
                buffer--;
                lo--;
            } else {
                // Locked ')'
                buffer++;
            }
            if (buffer < 0) {
                return false;
            }
            if (lo == 0) return true; // All locked '(' processed.
            if (u == 0) {
                // At this point, we've consumed all unlocked chars.
                // If there are still locked '(' remaining,
                // they need to be matched to whatever is in the buffer,
                // which at this time is purely made up of the locked ')'
                // we've revisited so far in the 2nd pass.
                // Any locked ')' on the left would've already
                // consumed a locked '(' in the 1st pass and decreased lo back then.
                // Put another way, remember we said before that we just need to match
                // the remaining u unlocked characters to remaining lo locked '('?
                // All we need to do now is to check if lo <= buffer.
                break;
            }
        }
        // System.out.printf("lo = %d, buffer = %d", lo, buffer);
        return lo <= buffer;
    }
}
