impl Solution {
    pub fn sort_people(names: Vec<String>, heights: Vec<i32>) -> Vec<String> {
        let mut zipped = names.iter().zip(heights.iter()).collect::<Vec<(&String, &i32)>>();
        zipped.sort_by_key(|a| -a.1)    ;
        // for (n, h) in &zipped {
        //     println!("({}, {})", n, h);
        // }
        zipped.iter().map(|&a| a.0.to_string()).collect()
    }
}
