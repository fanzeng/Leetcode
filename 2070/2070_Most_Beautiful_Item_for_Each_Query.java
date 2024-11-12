class Solution {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        int[] answer = new int[queries.length];
        Comparator<int[]> cp = (a, b) -> Integer.compare(a[0], b[0]);
        PriorityQueue<int[]> pqItem = new PriorityQueue<>(cp);
        for (int[] item : items) {
            pqItem.add(item);
        }
        PriorityQueue<int[]> pqQuery = new PriorityQueue<>(cp);
        for (int j = 0; j < queries.length; j++) {
            pqQuery.add(new int[]{queries[j], j});
        }

        int maxBeauty = 0;
        while (!pqQuery.isEmpty()) {
            int[] queryIndex = pqQuery.poll();
            int query = queryIndex[0];
            int index = queryIndex[1];
            // System.out.println("query: " + query + ", index: " + index); 
            answer[index] = maxBeauty;
            while (!pqItem.isEmpty()) {
                int[] item = pqItem.poll();
                int price = item[0];
                int beauty = item[1];
                // System.out.println("price: " + price + ", beauty: " + beauty); 
                if (price > query) {
                    pqItem.add(item);
                    break;
                } else if (beauty > maxBeauty) {
                    maxBeauty = beauty;
                    answer[index] = maxBeauty;
                }
            }
        }
        return answer;
    }
}
