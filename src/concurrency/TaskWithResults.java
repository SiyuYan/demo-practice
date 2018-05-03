package concurrency;

import java.util.concurrent.Callable;

class TaskWithResults implements Callable<String> {//Callable
    private static int taskCount = 0;
    private final int id = taskCount++;

    TaskWithResults() {
        System.out.println("Printer started 我, ID = " + id);
    }

    @Override
    public String call() throws Exception {
        return "result is" + id;
    }
}

