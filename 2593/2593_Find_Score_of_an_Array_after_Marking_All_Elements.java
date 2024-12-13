class Solution {
    public long findScore(int[] nums) {
        class Pair {
            int value;
            int index;
            public Pair(int value, int index) {
                this.value = value;
                this.index = index;
            }
        }
        Comparator<Pair> comparator = new Comparator<>() {
            @Override
            public int compare(Pair p1, Pair p2) {
                if (p1.value == p2.value) return Integer.compare(p1.index, p2.index);
                return Integer.compare(p1.value, p2.value);
            }
        };
        PriorityQueue<Pair> q = new PriorityQueue<>(comparator);
        boolean[] marked = new boolean[nums.length];
        for (int i = 0; i < nums.length; i++) {
            q.add(new Pair(nums[i], i));
        }
        long score = 0;
        while (!q.isEmpty()) {
            Pair p = q.poll();
            if (marked[p.index]) continue;
            marked[p.index] = true;
            if (p.index + 1 < marked.length) marked[p.index+1] = true;
            if (p.index > 0) marked[p.index-1] = true;
            score += p.value;
        }
        return score;
    }
}
