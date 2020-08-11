package java_test;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class file {
    public static void main(String[] args) throws IOException {
//        File file = null;
//        String[] paths;
//
//        file = new File("src");
//
//        paths = file.list();
//
//        assert paths != null;
//        for (String path : paths) {
//            System.out.println(path);
//        }
//--------------
//        File f = null;
//        String[] strs = {"src/java_test/output.txt", "src/java_test/input.txt"};
//        for (String s : strs) {
//            f = new File(s);
//            boolean bool = f.canExecute();
//            String a = f.getAbsolutePath();
//            System.out.print(a);
//            System.out.println(" is executable: " + bool);
//        }
//--------------
        File file = new File("src/java_test/test.txt");
        System.out.println("create success?:" + file.createNewFile());

        FileWriter writer = new FileWriter(file);

        writer.write("This\n is\n an\n example\n");
        writer.flush();
        writer.close();

        FileReader fr = new FileReader(file);
        char[] a = new char[50];
        System.out.println(fr.read(a));

        for (char c : a)
            System.out.print(c);
        fr.close();
    }
}
