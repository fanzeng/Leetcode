class Solution {
    public int countDays(int days, int[][] meetings) {
        Arrays.sort(meetings, (a, b) -> Integer.compare(a[0], b[0]));
        int i = -1;
        int res = meetings[0][0]-1;
        int end = meetings[0][1];
        while (++i < meetings.length-1) {
            int[] curr = meetings[i];
            int[] next = meetings[i+1];
            end = Math.max(end, curr[1]);
            if (end < next[0]) {
                res += next[0] - end - 1;
            }
        }
        end = Math.max(end, meetings[meetings.length-1][1]);
        res += days - end;
        return res;
    }
}
