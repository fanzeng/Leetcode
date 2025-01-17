class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        return testExist(derived, 1) || testExist(derived, 0);
    }
    private boolean testExist(int[] derived, int start) {
        int n = derived.length;
        int a = start;
        for (int i = 0; i < derived.length; i++) {
            a = a ^ derived[i];
        }
        return a == start;
    }
}
