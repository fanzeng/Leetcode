impl Solution {
    pub fn count_seniors(details: Vec<String>) -> i32 {
        details.into_iter().map(|p| (&p[11..13]).parse().unwrap()).filter(|age: &i32| *age > 60).collect::<Vec<_>>().len() as i32
    }
}
