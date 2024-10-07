impl Solution {
    pub fn min_length(s: String) -> i32 {
        let mut t = s.clone();
        let mut d;
        loop {
            (t, d) = Self::remove(&t);
            // print!("t = {}, d = {}\n", t, d);
            if !d {
                break
            }
        }
        t.len() as i32
    }
    fn remove(s: &String) -> (String, bool) {
        // print!("s = {}\n", s);
        let mut r = String::new();
        let mut d = false;
        let c: Vec<_> = s.chars().collect();
        let mut i = 0;
        while i < c.len() {
            if (i < c.len() - 1) && ((c[i] == 'A' && c[i+1] == 'B') || (c[i] == 'C' && c[i+1] == 'D')) {
                d = true;
                i += 1;
            } else {
                r.push(c[i]);
            }
            i += 1
        }
        (r, d)
    }
}
