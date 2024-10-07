class Solution {
    public String[] findWords(String[] words) {
        ArrayList<String> res = new ArrayList();
        String[] keys = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (var word : words) {
            var lword = word.toLowerCase();
            String key = "";
            for (var k : keys) {
                if (k.indexOf(lword.charAt(0)) >= 0) {
                    key = k;
                    break;
                }
            }
            boolean neg = false;
            for (var c : lword.toCharArray()) {
                if (key.indexOf(c) < 0) {
                    neg = true;
                }
            }
            if (!neg) {
                res.add(word);
            }
        }
        return res.toArray(new String[0]);
    }
}
