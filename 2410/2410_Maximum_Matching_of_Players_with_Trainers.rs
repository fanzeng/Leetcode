impl Solution {
    pub fn match_players_and_trainers(players: Vec<i32>, trainers: Vec<i32>) -> i32 {
        let mut p = players.clone();
        let mut t = trainers.clone();
        p.sort();
        t.sort();
        let mut i = 0;
        let mut j = 0;
        let mut res = 0;
        while (i < p.len() && j < t.len()) {
            if (t[j] >= p[i]) {
                i += 1;
                j += 1;
                res += 1;
            } else {
                j += 1;
            }
        }
        res
    }
}
