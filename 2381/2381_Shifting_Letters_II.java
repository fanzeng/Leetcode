class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        long[] totalShifts = new long[s.length()];
        List<int[]> events = new ArrayList<>();
        for (int i = 0; i < shifts.length; i++) {
            int[] shift = shifts[i];
            int start = shift[0];
            int end = shift[1];
            int delta = shift[2] == 1 ? 1 : 25;
            events.add(new int[]{start, delta});
            events.add(new int[]{end+1, 26-delta});
        }
        Collections.sort(events, new Comparator<int[]>() {
            @Override
            public int compare(int[] a, int[] b) {
                return Integer.compare(a[0], b[0]);
            }
        });
        int t = 0;
        int prev = -1;
        for (int i = 0; i < events.size(); i++) {
            int[] event = events.get(i);
            // System.out.println("event = " + Arrays.toString(event));
            boolean isNew = event[0] != prev;
            // System.out.printf("prev = %d, isNew = %b\n", prev, isNew);
            if (isNew) {
                t++;
                while (t <= event[0] && t < totalShifts.length) {
                    totalShifts[t] = t > 0 ? totalShifts[t-1] : 0;
                    t++;
                }
                t--;
            }
            if (event[0] == totalShifts.length) break;
            if (t >= 0 && t < totalShifts.length) {
                // System.out.printf("t = %d, event[1] = %d\n", t, event[1]);
                totalShifts[t] += event[1];
                // System.out.printf("totalShifts[%d] = %d\n", t, totalShifts[t]);
            }
            prev = t;
        }
        // System.out.println("totalShifts = " + Arrays.toString(totalShifts));
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.append((char)('a' + ((s.charAt(i) - 'a' + totalShifts[i]) % 26)));
        }
        return sb.toString();
    }
}
