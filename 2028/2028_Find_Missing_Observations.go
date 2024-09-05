func missingRolls(rolls []int, mean int, n int) []int {
    m := len(rolls)
    sum := mean * (m + n)
    for _, r := range(rolls) {
        sum -= r
    }
    // fmt.Println(sum)
    if sum < n || sum > n*6 {
        return []int{}
    }
    floor := sum / n
    diff := sum - floor*n
    lo := make([]int, n - diff)
    hi := make([]int, diff)
    for i := 0; i < n - diff; i++ {
        lo[i] = floor
    }
    for i := 0; i < diff; i++ {
        hi[i] = floor + 1
    }
    return append(lo, hi...)
}
