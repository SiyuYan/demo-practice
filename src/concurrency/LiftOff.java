package concurrency;
class LiftOff implements Runnable {
    private static int taskCount = 0;
    private final int id = taskCount++;

    LiftOff() {
        System.out.println("Printer started 我, ID = " + id);
    }

    @Override
    public void run() {
        System.out.println("Stage 1..爱., ID = " + id);
//        Thread.yield();
//        Thread.sleep(100);
        System.out.println("Stage 2..你., ID = " + id);
        Thread.yield();
        System.out.println("Stage 3..不., ID = " + id);
        Thread.yield();
        System.out.println("Printer ended傻, ID = " + id);
    }

}

