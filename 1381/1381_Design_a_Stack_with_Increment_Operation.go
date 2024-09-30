type CustomStack struct {
    a []int
    c int
}


func Constructor(maxSize int) CustomStack {
    return CustomStack{c: maxSize}
}


func (this *CustomStack) Push(x int)  {
    if len(this.a) < this.c {
        this.a = append(this.a, x)
    }
}


func (this *CustomStack) Pop() int {
    if len(this.a) == 0 {
        return -1
    }
    s, x := this.a[:len(this.a) - 1], this.a[len(this.a) - 1]
    this.a = s
    return x
}


func (this *CustomStack) Increment(k int, val int)  {
    for i := 0; i < k; i++ {
        if i == len(this.a) {
            break
        }
        this.a[i] += val
    }
}


/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
