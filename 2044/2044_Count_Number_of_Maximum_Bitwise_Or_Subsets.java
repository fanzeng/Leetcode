class Solution {
    public int countMaxOrSubsets(int[] nums) {
        if (nums.length < 2) return 1;
        int bor = nums[0] | nums[1];
        for (int i = 2; i < nums.length; i++) {
            // System.out.printf("bor = %d\n", bor);
            bor = bor | nums[i];
        }
        // Print the maximum bitwise OR value
        // System.out.printf("bor = %d\n", bor);
        return countSubsets(nums, bor);
    }

    // a: The array
    // t: The maximum bitwise OR
    int countSubsets(int[] a, int t) {
        if (a.length == 1) return 1; // If there is only 1 element, t must be that element, so 1 subset
        int count = 0;
        // Now we have at least 2 elements in the array.
        // This array stores bitwise ORs of all subarrays after i
        ArrayList<Integer> bors = new ArrayList();
        bors.add(a[a.length-1]); // Initialise to contain the last element.
        if (a[a.length-1] == t) count++;
        for (int i = a.length - 2; i > -1; i--) {
            int n = a[i];
            if (n == t) count++;
            ArrayList<Integer> newBors = new ArrayList();
            newBors.add(n);
            for (int j = 0; j < bors.size(); j++) {
                int bor = bors.get(j);
                int newBor = n | bor;
                newBors.add(newBor);
                if (newBor == t) count++;
            }
            bors.addAll(newBors);
        }
        return count;
    }
}
