type MyCalendarTwo struct {
    a [][]int // Will be sorted by start
}


func Constructor() MyCalendarTwo {
    return MyCalendarTwo{}
}


func (this *MyCalendarTwo) Book(start int, end int) bool {
    // fmt.Printf("[%d, %d]\n", start, end)
    // fmt.Printf("this.a = %d\n", this.a)
    count := 0
    var e int // End of first double book
    for _, b := range this.a {
        // Find the 1st inteval that may cause problem
        if b[1] <= start {
            continue
        }
        // Those start later than our end won't cause issue
        // And since we sort by start time, we are done
        if b[0] >= end {
            break
        }
        // Now we have an interval ending after we start, and starting before our end,
        // which is an overlapping interval
        // fmt.Printf("overlap with = %v\n", b)
        if count > 0 {
            if b[0] < e {
                return false
            }
        }
        e = b[1]
        count++
    }
    var i int
    for i < len(this.a) {
        b := this.a[i]
        if b[0] >= start {
            break
        }
        i++
    }
    if i < len(this.a) {
        temp := this.a[i:]
        this.a = append(this.a[:i], append([][]int{[]int{start, end}}, temp...)...)
    } else {
        this.a = append(this.a, []int{start, end}) 
    }
    return true
}


/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
