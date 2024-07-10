func averageWaitingTime(customers [][]int) float64 {
    curr := 0
    wait := 0
    for _, c := range(customers) {
        s, t := c[0], c[1]
        if s > curr {
            curr = s
        }
        curr += t
        wait += curr - s
    }
    return float64(wait) / float64(len(customers))
}
