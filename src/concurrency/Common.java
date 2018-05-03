package concurrency;

class Common {
    private static int taskCount = 0;
    private final int id = taskCount++;
    Common() {
        System.out.println("Printer started, ID = " + id);
    }

    public void run() {
        System.out.println("Stage 1..., ID = " + id);
        Thread.yield();
        System.out.println("Stage 2..., ID = " + id);
        Thread.yield();
        System.out.println("Stage 3..., ID = " + id);
        Thread.yield();
        System.out.println("Printer ended, ID = " + id);
    }
}
