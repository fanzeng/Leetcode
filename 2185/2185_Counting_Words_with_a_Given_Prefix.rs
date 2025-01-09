impl Solution {
    pub fn prefix_count(words: Vec<String>, pref: String) -> i32 {
        words.into_iter().filter(|w| w.starts_with(&pref)).collect::<Vec<_>>().len().try_into().unwrap()
    }
}
