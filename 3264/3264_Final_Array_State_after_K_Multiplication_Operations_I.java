class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        class Pair {
            int value;
            int index;
            public Pair(int value, int index) {
                this.value = value;
                this.index = index;
            }
        }
        PriorityQueue<Pair> q = new PriorityQueue<>(
            new Comparator<>() {
                @Override
                public int compare(Pair p1, Pair p2) {
                    if (p1.value == p2.value) return Integer.compare(p1.index, p2.index);
                    return Integer.compare(p1.value, p2.value);
                }
            }
        );
        for (int i = 0; i < nums.length; i++) {
            q.add(new Pair(nums[i], i));
        }
        int count = 0;
        while (!q.isEmpty() && count++ < k) {
            Pair pair = q.poll();
            int newValue = pair.value*multiplier;
            nums[pair.index] = newValue;
            q.add(new Pair(newValue, pair.index));
        }
        return nums;
    }
}
