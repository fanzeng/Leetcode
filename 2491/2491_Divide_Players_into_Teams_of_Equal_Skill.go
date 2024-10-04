func dividePlayers(skill []int) int64 {
    s := 0
    m := make(map[int]int)
    for _, a := range skill {
        s += a
        if _, exists := m[a]; !exists {
            m[a] = 0
        }
        m[a]++
    }
    if s % (len(skill) / 2) != 0 {
        return -1
    }
    t := s / (len(skill) / 2)
    var p int64 = 0
    for _, a := range skill {
        if count, exists := m[t - a]; !exists || count == 0 {
            return -1
        }
        m[t - a] -= 1
        p += int64(a * (t - a))
    }
    return p / 2
}
