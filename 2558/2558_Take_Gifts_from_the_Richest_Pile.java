class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer> q = new PriorityQueue<>(Comparator.reverseOrder());
        for (int g : gifts) {
            q.add(g);
        }
        for (int i = 0; i < k; i++) {
            int g = q.poll();
            q.add((int)Math.sqrt(g));
        }
        long s = 0;
        while (!q.isEmpty()) {
            int g = q.poll();
            s += g;
        }
        return s;
    }
}
