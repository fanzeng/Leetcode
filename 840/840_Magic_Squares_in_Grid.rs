impl Solution {
    // the sum of 1 to 9 is 45
    // the 3 rows in a magic square have equal sum
    // and the numbers are unique
    // this means the "same sum" is 15
    // now conside3r the + in the middle of the magic square and the 2 diagonals
    // the sum of these 4 triplets is 60
    // on the other hand, all 9 grid points are used exactly once except the center
    // which is used 4 times
    // so 60 - 45 = 15 is 3 times the value of the center grid point
    // which means the center should always be 5
    pub fn num_magic_squares_inside(grid: Vec<Vec<i32>>) -> i32 {
        if grid.len() < 3 {
            return 0;
        }
        if grid[1].len() < 3 {
            return 0;
        }
        let mut res = 0;
        for i in 1..grid.len()-1 {
            for j in 1..grid[0].len()-1 {
                if grid[i][j] != 5 {
                    continue
                }
                if Self::check(&grid, i, j) {
                    res += 1;
                }
            }
        }
        res
    }
    fn check(grid: &Vec<Vec<i32>>, i: usize, j: usize) -> bool {
        if Self::sum(grid, i-1, j-1, i-1, j, i-1, j+1) != 15 {
            return false;
        }
        if Self::sum(grid, i, j-1, i, j, i, j+1) != 15 {
            return false;
        }
        if Self::sum(grid, i+1, j-1, i+1, j, i+1, j+1) != 15 {
            return false;
        }
        if Self::sum(grid, i-1, j-1, i, j-1, i+1, j-1) != 15 {
            return false;
        }
        if Self::sum(grid, i-1, j, i, j, i+1, j) != 15 {
            return false;
        }
        if Self::sum(grid, i-1, j+1, i, j+1, i+1, j+1) != 15 {
            return false;
        }
        if Self::sum(grid, i-1, j-1, i, j, i+1, j+1) != 15 {
            return false;
        }
        if Self::sum(grid, i+1, j+1, i, j, i-1, j-1) != 15 {
            return false;
        }
        let mut v = vec![0; 9];
        for r in (i-1)..(i+2) {
            for c in (j-1)..(j+2) {
                if grid[r][c] < 1 || grid[r][c] > 9 {
                    return false;
                }
                v[(grid[r][c]-1) as usize] += 1;
            }
        }
        for k in 0..9 {
            if v[k] != 1 {
                return false;
            }
        }
        true
    }
    fn sum(grid: &Vec<Vec<i32>>, r0: usize, c0: usize, r1: usize, c1: usize, r2: usize, c2: usize) -> i32 {
        return grid[r0][c0] + grid[r1][c1] + grid[r2][c2];
    }
}
