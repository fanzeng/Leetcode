class Solution {
    public String removeOccurrences(String s, String part) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            stack.push(c);
            if (stack.size() >= part.length()) {
                if (check(stack, part)) {
                    for (int i = 0; i < part.length(); i++) {
                        stack.pop();
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < stack.size(); i++) {
            sb.append(stack.get(i));
        }
        return sb.toString();
    }
    private boolean check(Stack<Character> stack, String part) {
        for (int i = 0; i < part.length(); i++) {
            if (stack.get(stack.size()-part.length()+i) != part.charAt(i)) return false;
        }
        return true;
    }
}
