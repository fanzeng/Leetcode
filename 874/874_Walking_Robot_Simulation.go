import "sort"

func robotSim(commands []int, obstacles [][]int) int {
    d := 0
    mx := make(map[int][]int)
    my := make(map[int][]int)
    for _, o := range(obstacles) {
        x, y := o[0], o[1]
        if _, exists := mx[x]; !exists {
            mx[x] = []int{}
        }
        mx[x] = append(mx[x], y)
        if _, exists := my[y]; !exists {
            my[y] = []int{}
        }
        my[y] = append(my[y], x)
    }
    for _, v := range(mx) {
        sort.Ints(v)
    }
    for _, u := range(my) {
        sort.Ints(u)
    }
    // fmt.Printf("mx = %v, my = %v\n", mx, my)
    r := rob{0, 0, 1, mx, my, false}
    for _, c := range(commands) {
        r.move(c)
        if !r.moved && (r.x != 0 || r.y != 0) {
            r.moved = true
        }
        // fmt.Printf("(%d, %d, %d), ", r.x, r.y, r.a)
        dist := r.getDist()
        if dist > d {
            d = dist
        }
    }
    return d
}

type rob struct {
    x int
    y int
    a int // Angle: 0: 0deg, 1: 90deg, 2: 180deg, 3: 270deg
    mx map[int][]int
    my map[int][]int
    moved bool
}

func (r rob) getDist() int {
    return r.x*r.x + r.y*r.y
}

func (r *rob) move(c int) {
    if c > 0 {
        switch r.a {
            case 0:
                r.x = minBetween(r.my[r.y], r.x, r.x + c, !r.moved) - 1
            case 1:
                r.y = minBetween(r.mx[r.x], r.y, r.y + c, !r.moved) - 1
            case 2:
                r.x = maxBetween(r.my[r.y], r.x - c, r.x, !r.moved) + 1
            case 3:
                r.y = maxBetween(r.mx[r.x], r.y - c, r.y, !r.moved) + 1
        }
    } else if c == -1 {
        r.a = (r.a + 3) % 4
    } else {
        r.a = (r.a + 1) % 4
    }
}

// Find the min element in ascending-sorted array which is > a and <= b
// If no such element return b + 1
// Can use binary search if slice is long
// But it might not be necessary because the step length is at most 9
func minBetween(arr []int, a, b int, ignoreZero bool) int {
    // fmt.Printf("%v, %d, %d", arr, a, b)
    for _, n := range(arr) {
        if n > a && n <= b && !(ignoreZero && n == 0) {
            return n
        }
    }
    return b + 1
}

// Find the max element in ascending-sorted array which is >= a and < b
// If no such element return a - 1
// Can use binary search if slice is long
// But it might not be necessary because the step length is at most 9
func maxBetween(arr []int, a, b int, ignoreZero bool) int {
    for i := len(arr)-1; i > -1; i-- {
        n := arr[i]
        if n >= a && n < b && !(ignoreZero && n == 0) {
            return n
        }
    }
    return a - 1
}
