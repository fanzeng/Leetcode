use std::collections::HashMap;
impl Solution {
    pub fn kth_distinct(arr: Vec<String>, k: i32) -> String {
        let mut m = HashMap::new();
        for s in &arr {
            let count = m.entry(s).and_modify(|count| *count += 1).or_insert(1);
        }
        let mut i = 0;
        for s in &arr {
            if m[s] == 1 {
                i += 1;
            }
            if i == k {
                return s.clone();
            }
        }
        String::new()
    }
}
