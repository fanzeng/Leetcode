class Solution {
    public String compressedString(String word) {
        StringBuilder sb = new StringBuilder();
        if (word.length() < 1) return word;
        char prev = word.charAt(0);
        int count = 1;
        for (int i = 1; i < word.length(); i++) {
            char c = word.charAt(i);
            count++;
            if (prev != c || count == 10) {
                sb.append(Integer.toString(count-1));
                sb.append(prev);
                count = 1;
            }
            prev = c;
        }
        sb.append(Integer.toString(count));
        sb.append(word.charAt(word.length()-1));
        return sb.toString();
    }
}
