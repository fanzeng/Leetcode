class Solution {
    public String pushDominoes(String dominoes) {
        char[] arr = dominoes.toCharArray();
        int n = arr.length;
        int[] forces = new int[n];

        int force = 0;
        // Left to right pass
        for (int i = 0; i < n; i++) {
            if (arr[i] == 'R') {
                force = n; // maximum force
            } else if (arr[i] == 'L') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            forces[i] += force;
        }

        // Right to left pass
        force = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] == 'L') {
                force = n;
            } else if (arr[i] == 'R') {
                force = 0;
            } else {
                force = Math.max(force - 1, 0);
            }
            forces[i] -= force;
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (forces[i] > 0) {
                result.append('R');
            } else if (forces[i] < 0) {
                result.append('L');
            } else {
                result.append('.');
            }
        }
        return result.toString();
    }
}
