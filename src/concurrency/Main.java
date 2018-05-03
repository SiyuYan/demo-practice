package concurrency;

import java.util.ArrayList;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Main {
    public static void main(String[] args) {
//        ExecutorService executorService = Executors.newCachedThreadPool();
//        ExecutorService executorService = Executors.newFixedThreadPool(4);
//        ExecutorService executorService = Executors.newSingleThreadExecutor();

//        for (int i = 0; i < 5; i++) {
//            new Common().run();   // One thread
//            new Thread(new LiftOff()).start();  // 1. Thread Class
//            new LiftOff().run(); // 2. Runnable Class run method
//            executorService.execute(new LiftOff()); // 3. Executor thread pool
//        }
//        executorService.shutdown();

        ExecutorService executorService = Executors.newCachedThreadPool();
        ArrayList<Future<String>> results = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            results.add(executorService.submit(new TaskWithResults()));
        }
        results.forEach((item) -> {
            try {
                System.out.println(item.get());
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        });
        executorService.shutdown();

    }
}
