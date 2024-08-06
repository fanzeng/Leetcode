use std::collections::HashMap;
impl Solution {
    pub fn minimum_pushes(word: String) -> i32 {
        
        let mut counts = HashMap::new();
        for c in word.chars() {
            // println!("c = {}", c);
            let mut c = counts.entry(c).or_insert(0);
            *c += 1;
        }
        let mut press = 1;
        let mut items = counts.iter().collect::<Vec<_>>();
        items.sort_by(|a, b| b.1.cmp(a.1));
        let mut res: i32 = 0;
        let mut used = 0;
        for item in items {
            // println!("item = {:?}", item);
            res += press * item.1;
            used += 1;
            if used == 8 {
                used = 0;
                press += 1
            }
        }
        res
    }
}
