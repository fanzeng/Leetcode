func findMinDifference(timePoints []string) int {
    res := 60*24
    values := make([]int, len(timePoints))
    for i, t := range timePoints {
        values[i] = getValue(t)
    }
    sort.Ints(values)
    for i := 0; i < len(values) - 1; i++ {
        diff := values[i+1] - values[i]
        if diff < res {
            res = diff
        }
    }
    diff_circ := values[0] - (values[len(values)-1] - 60*24)
    if diff_circ < res {
        res = diff_circ
    }
    return res
}

func getValue(t string) int {
    s := strings.Split(t, ":")
    h, _ := strconv.Atoi(s[0])
    m, _ := strconv.Atoi(s[1])
    return h*60 + m
}
