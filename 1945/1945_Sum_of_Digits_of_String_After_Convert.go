import (
    "strconv"
    "math/big"
)

func getLucky(s string, k int) int {
    t := ""
    for _, c := range(s) {
        t += strconv.Itoa(int(c - 'a' + 1))
    } 
    // fmt.Printf("%s\n", t)
    big := new(big.Int)
    big, _ = big.SetString(t, 10)
    res := reduce(big)
    if k == 1 {
        return res
    }
    for _ = range(k-1) {
        res = reduce(res)
    }
    return res
}

func reduce(s interface{}) int {
    // fmt.Printf("%d\n", s)
    var t string
    switch s := s.(type) {
        case int:
            t = strconv.Itoa(s)
        case *big.Int:
            t = s.String()
    }
    sum := 0
    // fmt.Printf("%s\n", t)
    for _, r := range(t) {
        sum += int(r - '0')
    }
    return sum
}
