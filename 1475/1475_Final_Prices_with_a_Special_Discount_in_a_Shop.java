class Solution {
    public int[] finalPrices(int[] prices) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < prices.length; i++) {
            int curr = prices[i];
            while (!stack.isEmpty()) {
                if (prices[stack.peek()] >= curr) {
                    int j = stack.pop();
                    prices[j] -= curr;
                } else {
                    break;
                }
            }
            stack.push(i);
        }
        return prices;
    }
}
