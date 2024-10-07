class Solution {
    public int thirdMax(int[] nums) {
        int m1 = Integer.MIN_VALUE;
        for (int n: nums) {
            if (n > m1) {
                m1 = n;
            }
        }
        // System.out.println("m1 = " + m1);
        int m2 = Integer.MIN_VALUE;
        for (int n: nums) {
            if (n != m1 && n > m2) {
                m2 = n;
            }
        }
        // System.out.println("m2 = " + m2);
        int m3 = Integer.MIN_VALUE;
        boolean found = false;
        for (int n: nums) {
            if (n != m1 && n != m2 && n >= m3) {
                m3 = n;
                found = true;
            }
        }
        // System.out.println("m3 = " + m3);
        if (!found) {
            return m1;
        }
        return m3;
    }
}
