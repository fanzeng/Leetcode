class Solution {
    public String addSpaces(String s, int[] spaces) {
        StringBuilder sb = new StringBuilder();
        char[] ch = s.toCharArray();
        int j = 0;
        int sp = spaces[j];
        for (int i = 0; i < ch.length; i++) {
            if (i == sp) {
                sb.append(' ');
                j++;
                if (j == spaces.length) {
                    sp = -1;
                } else {
                    sp = spaces[j];
                }
            }
            sb.append(ch[i]);
        }
        return sb.toString();
        
    }
}
