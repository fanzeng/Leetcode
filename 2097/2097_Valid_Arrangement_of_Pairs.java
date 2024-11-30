class Solution {
    public int[][] validArrangement(int[][] pairs) {
        HashMap<Integer, LinkedList<Integer>> adj = new HashMap<>();
        HashMap<Integer, Integer> inDeg = new HashMap<>();
        HashMap<Integer, Integer> outDeg = new HashMap<>();
        for (int i = 0; i < pairs.length; i++) {
            int s = pairs[i][0];
            int t = pairs[i][1];
            adj.putIfAbsent(s, new LinkedList<>());
            adj.get(s).add(t);
            inDeg.put(t, inDeg.getOrDefault(t, 0)+1);
            outDeg.put(s, outDeg.getOrDefault(s, 0)+1);
        }
        int s = getStart(inDeg, outDeg);
        if (s == -1) s = pairs[0][0];
        ArrayList<Integer> res = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        stack.push(s);
        while(!stack.empty()) {
            int v = stack.peek();
            if (adj.getOrDefault(v, new LinkedList<>()).size() > 0) {
                int u = adj.get(v).removeFirst();
                stack.push(u);
            } else {
                res.add(v);
                stack.pop();
            }
        }
        Collections.reverse(res);
        int[][] ans = new int[res.size()-1][2];
        for (int i = 1; i < res.size(); i++) {
            ans[i-1][0] = res.get(i-1);
            ans[i-1][1] = res.get(i);
        }
        return ans;
    }
    private int getStart(HashMap<Integer, Integer> inDeg, HashMap<Integer, Integer> outDeg) {
        int s = -1;
        Set<Integer> ks = outDeg.keySet();
        for (int k : ks) {
            if (outDeg.get(k) == inDeg.getOrDefault(k, 0) + 1) {
                s = k;
                return s;
            }
        }
        return s;
    }
}
