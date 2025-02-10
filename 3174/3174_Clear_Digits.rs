impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut stack: Vec<char> = Vec::new();
        for c in s.chars() {
            if c.is_digit(10) && !stack.is_empty() {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        stack.iter().collect()
    }
}
