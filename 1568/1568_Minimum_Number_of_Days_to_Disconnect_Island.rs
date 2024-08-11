impl Solution {
    pub fn min_days(grid: Vec<Vec<i32>>) -> i32 {
        if !Self::exists_island(&grid) {
            return 0
        }
        let (res, dict) = Self::is_single_island(&grid);
        if !res {
            return 0
        }
        if Self::get_island_size(&dict) == 2 {
            return 2
        }
        if Self::get_island_size(&dict) == 1 {
            return 1
        }
        // Check for any single-neighbor pixel
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if dict[i][j] == 2 {
                    let nc = Self::get_neighbor_count(&grid, i, j);
                    if nc == 1 {
                        return 1;
                    }
                }
            }
        } 
        // Check for any double-neighbor pixel
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if dict[i][j] == 2 {
                    let nc = Self::get_neighbor_count(&grid, i, j);
                    if nc == 2 {
                        let mut test_grid = grid.clone();
                        test_grid[i][j] = 0;
                        let (test_res, _) = Self::is_single_island(&test_grid);
                        if !test_res {
                            return 1;
                        }
                    }
                }
            }
        } 
        // Deal with the remaining cases
        for i in 0..grid.len() {
            for j in 0..grid[0].len() {
                if dict[i][j] == 2 {
                    let nc = Self::get_neighbor_count(&grid, i, j);
                    if nc > 2 {
                        let mut test_grid = grid.clone();
                        test_grid[i][j] = 0;
                        let (test_res, _) = Self::is_single_island(&test_grid);
                        if !test_res {
                            return 1;
                        }
                    }
                }
            }
        } 
        2
    }
    fn is_single_island(grid: &Vec<Vec<i32>>) -> (bool, Vec<Vec<i32>>) {
        let mut dict: Vec<Vec<i32>> = Vec::new();
        let mut l = 2; // Use 2 as label but can be anything.
        for i in 0..(*grid).len() {
            dict.push(vec![-1; (*grid[0]).len()])
        }
        for i in 0..(*grid).len() {
            for j in 0..(*grid)[0].len() {
                if (*grid)[i][j] == 1 {
                    Self::label_island(grid, &mut dict, i, j, l);
                    l += 1;
                    break
                }
            }
            if l > 2 {
                break
            }
        } 
        for i in 0..(*grid).len() {
            for j in 0..(*grid)[0].len() {
                if (*grid)[i][j] == 1 && dict[i][j] == -1 {
                    // println!("Found 2nd island at ({}, {}).", i, j);
                    // println!("dict: {:?}", dict);
                    return (false, dict)
                }
            }
        } 
        (true, dict)
    }
    fn label_island(grid: &Vec<Vec<i32>>, dict: &mut Vec<Vec<i32>>, i: usize, j: usize, l: i32) {
        (*dict)[i][j] = l;
        if i+1 < grid.len() && grid[i+1][j] == 1 && dict[i+1][j] == -1 {
            Self::label_island(grid, dict, i+1, j, l);
        }
        if j+1 < grid[0].len() && grid[i][j+1] == 1 && dict[i][j+1] == -1 {
            Self::label_island(grid, dict, i, j+1, l);
        }
        if i as i32 -1 >= 0 && grid[i-1][j] == 1 && dict[i-1][j] == -1 {
            Self::label_island(grid, dict, i-1, j, l);
        }
        if j as i32 - 1 >= 0 && grid[i][j-1] == 1 && dict[i][j-1] == -1 {
            Self::label_island(grid, dict, i, j-1, l);
        }
        // println!("dict:{:?}", dict);
    }
    fn get_island_size(dict: &Vec<Vec<i32>>) -> i32 {
        let mut size = 0;
        for i in 0..dict.len() {
            for j in 0..dict[0].len() {
                if dict[i][j] != -1 {
                    size += 1;
                }
            }
        }
        size
    }
    fn get_neighbor_count(grid: &Vec<Vec<i32>>, i: usize, j: usize) -> i32 {
        let mut count = 0;
        if i as i32 - 1 >= 0 && (*grid)[i-1][j] == 1 {
            count += 1;
        }
        if j as i32 - 1 >= 0 && (*grid)[i][j-1] == 1 {
            count += 1;
        }
        if i + 1 < grid.len() && (*grid)[i+1][j] == 1 {
            count += 1;
        }
        if j + 1 < grid[0].len() && (*grid)[i][j+1] == 1 {
            count += 1;
        }
        count
    }
    fn exists_island(grid: &Vec<Vec<i32>>) -> bool {
        for i in 0..(*grid).len() {
            for j in 0..(*grid)[0].len() {
                if (*grid)[i][j] == 1 {
                    return true
                }
            }
        }
        false
    }
}
