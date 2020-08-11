package java_test;


import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.Stream;

public class collection_test {
    public static void main(String args[]) {
        // Create an Array
        String array[] = {"Geeks", "forGeeks",
                "A computer Portal"};
        ArrayList<String> arr_list = new ArrayList<>();
        arr_list.addAll(Arrays.asList(
                array
        ));

        arr_list.add("ssss");

        List list = Arrays.asList(array);
        System.out.println(arr_list);
        Arrays.sort(array);
        Collections.sort(arr_list);
    }
}
