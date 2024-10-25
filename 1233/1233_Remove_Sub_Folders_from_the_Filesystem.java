class Solution {
    HashSet<String> hs = new HashSet<>();
    public List<String> removeSubfolders(String[] folder) {
        for (String f : folder) {
            hs.add(f);
        }
        // hs.stream().forEach(System.out::println);
        List<String> res = new ArrayList<>();
        for (String f : folder) {
            // System.out.println(f);
            if (!isSubFolder(f)) res.add(f);
        }
        return res;
    }
    boolean isSubFolder(String f) {
        int lastSlash = f.lastIndexOf('/');
        while (lastSlash > 0) {
            f = f.substring(0, lastSlash);
            if (hs.contains(f)) return true;
            lastSlash = f.lastIndexOf('/');
        }
        return false;
    }
}
