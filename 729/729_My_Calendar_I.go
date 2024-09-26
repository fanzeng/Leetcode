type MyCalendar struct {
    a [][]int
}


func Constructor() MyCalendar {
   return MyCalendar{}
}


func (this *MyCalendar) Book(start int, end int) bool {
    for _, b := range this.a {
        if b[1] <= start {
            continue
        }
        if end > b[0] {
            return false
        }
    }
    this.a = append(this.a, []int{start, end})
    return true
}


/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
