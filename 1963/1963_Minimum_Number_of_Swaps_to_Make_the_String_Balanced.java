class Solution {
    public int minSwaps(String s) {
        int res = 0;
        int countOpen = 0;
        int countClose = 0;
        int j = s.length() - 1;
        char[] ca = s.toCharArray();
        for (int i = 0; i < ca.length; i++) {
            if (ca[i] == '[') {
                countOpen++;
            } else {
                countClose++;
            }
            // System.out.printf("countOpen = %d, countClose = %d\n", countOpen, countClose);
            if (countClose > countOpen) {
                countOpen++;
                countClose--;
                while (ca[j] != '[') {
                    j--;
                }
                ca[j] = ']';
                res++;
                if (i >= j) {
                    break;
                }
            }
        }
        return res;
    }
}
