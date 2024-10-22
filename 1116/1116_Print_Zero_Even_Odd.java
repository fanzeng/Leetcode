class ZeroEvenOdd {
    private int n;
    private boolean isNextEven;
    private boolean numberPrinted = true;
    private boolean zeroPrinted;
    private int num = 1;

    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public synchronized void zero(IntConsumer printNumber) throws InterruptedException {
        while (num <= n) {
            while (!numberPrinted) wait();
            if (num <= n) printNumber.accept(0);
            zeroPrinted = true;
            numberPrinted = false;
            notifyAll();
        }
    }

    public synchronized void even(IntConsumer printNumber) throws InterruptedException {
        while (num <= n) {
            while (!zeroPrinted || !isNextEven) wait();
            if (num <= n) printNumber.accept(num++);
            isNextEven = false;
            numberPrinted = true;
            zeroPrinted = false;
            notifyAll();
        }
    }

    public synchronized void odd(IntConsumer printNumber) throws InterruptedException {
        while (num <= n) {
            while (!zeroPrinted || isNextEven) wait();
            if (num <= n) printNumber.accept(num++);
            isNextEven = true;
            numberPrinted = true;
            zeroPrinted = false;
            notifyAll();
        }
    }
}
