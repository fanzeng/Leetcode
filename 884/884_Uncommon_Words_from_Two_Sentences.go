func uncommonFromSentences(s1 string, s2 string) []string {
    words1 := strings.Split(s1, " ")
    words2 := strings.Split(s2, " ")
    // fmt.Printf("words1 = %v, words2 = %v\n", words1, words2)
    res := make([]string, 0)
    m1 := make(map[string]int)
    m2 := make(map[string]int)
    for _, w := range words1 {
        if _, exists := m1[w]; !exists {
            m1[w] += 1
        } else {
            m1[w] = 0
        }
    }
    for _, w := range words2 {
        if _, exists := m2[w]; !exists {
            m2[w] += 1
        } else {
            m2[w] = 0
        }
    }
    // fmt.Printf("m1 = %v, m2 = %v\n", m1, m2)
    for _, w := range words2 {
        if count, _ := m2[w]; count == 1 {
            if _, exists := m1[w]; !exists {
                res = append(res, w)
            }
        }
    }
    for _, w := range words1 {
        if count, _ := m1[w]; count == 1 {
            if _, exists := m2[w]; !exists {
                res = append(res, w)
            }
        }
    }
    return res
}
