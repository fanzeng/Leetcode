impl Solution {
    pub fn count_prefix_suffix_pairs(words: Vec<String>) -> i32 {
        let mut count = 0;
        for (i, w) in words.iter().enumerate() {
            for j in i+1..words.len() {
                if Self::is_prefix_and_suffix(w, &words[j]) {
                    count += 1;
                }
            }
        }
        count
    }
    fn is_prefix_and_suffix(w0: &String, w1: &String) -> bool {
        if w1.starts_with(w0) && w1.ends_with(w0) {
            return true
        }
        false
    }
}
