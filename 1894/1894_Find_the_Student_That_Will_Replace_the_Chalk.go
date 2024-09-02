func chalkReplacer(chalk []int, k int) int {
    n := len(chalk)
    s := 0
    p := make([]int, n)
    for i, c := range(chalk) {
        s += c
        p[i] = s
    }
    k %= s
    // Find the first i s.t. p[i] > k
    l := 0
    r := n - 1
    m := (l + r) / 2
    for l + 1 < r {
        if p[m] <= k {
            l = m
        } else if p[m] > k {
            r = m
        }
        m = (l + r) / 2
    }
    if p[m] > k {
        return m
    }
    return r
}
