class Foo {

    public Foo() {
        
    }

    private boolean firstHasRun = false;
    private boolean secondHasRun = false;

    public void first(Runnable printFirst) throws InterruptedException {
        synchronized(this) {
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
            firstHasRun = true;
            notifyAll();
        }
    }

    public void second(Runnable printSecond) throws InterruptedException {
        synchronized(this) {
            while (!firstHasRun) wait();
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
            secondHasRun = true;
            notifyAll();
        }
    }

    public void third(Runnable printThird) throws InterruptedException {
        synchronized(this) {
            while (!secondHasRun) wait();
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
        }
    }
}
