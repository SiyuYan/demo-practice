package java_test;

import java.io.*;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class io {
    public static void main(String[] args) throws IOException {
//        FileInputStream input = null;
//        FileOutputStream output = null;
        FileReader input = null;
        FileWriter output = null;
        try {
//            input = new FileInputStream("src/java_test/input.txt");
//            output = new FileOutputStream("src/java_test/output.txt");

            String fileName = "input.txt";
            String path = findFile(new File(new File("").getAbsolutePath()), fileName);
            List<String> content = Files.readAllLines(Paths.get(path));

            System.out.println(content.size());


            input = new FileReader(fileName);
            output = new FileWriter("output.txt");
            int c = 0;
            while ((c = input.read()) != -1) {
                output.write(c);
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } finally {
            if (input != null) {
                input.close();
            }
            if (output != null) {
                output.close();
            }
        }
////---------------
//        InputStreamReader cin = null;
//        cin = new InputStreamReader(System.in);
//        System.out.println("q exit");
//        char c;
//        do {
//            c = (char) cin.read();
//            System.out.print(c);
//        } while (c != 'q');
//        cin.close();
////---------------

//        byte[] bWrite = {11, 21, 3, 40, 5};
//        OutputStream os = new FileOutputStream("src/java_test/output.txt");
//        for (byte b : bWrite) {
//            os.write(b);
//        }
//        os.close();
//
//        InputStream is = new FileInputStream("src/java_test/input.txt");
//        int size = is.available();
//
//        for (int i = 0; i < size; i++) {
//            System.out.print((char)is.read() + "  ");
//        }
//        is.close();

    }

    private static String findFile(File rootpath, String name) {

        File[] list = rootpath.listFiles();
        if (list != null) {
            for (File fil : list) {
                if (fil.isDirectory()) {
                    String path = findFile(fil, name);
                    if (path != null && !path.isEmpty()) {
                        return path;
                    }
                } else if (name.contains(fil.getName())) {
                    return fil.getAbsolutePath();
                }
            }
        }
        return null;
    }
}

