impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        let mut sorted_words = words.clone();
        sorted_words.sort_by(|a, b| a.len().cmp(&b.len()));
        let mut res = Vec::new();
        for (i, word) in sorted_words.iter().enumerate() {
            for j in i+1..sorted_words.len() {
                if sorted_words[j].contains(word.as_str()) {
                    res.push(word.clone());
                    break;
                }
            }
        }
        res
    }
}
