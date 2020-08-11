package java_test;

import java.util.*;
import java.util.stream.Collectors;

public class test {

    public static void main(String arg[]) {
        String S = "Forget. CVs..save time? .   x x!";

        String[] sentences = S.split("[.?!]");

        ArrayList<Integer> length = new ArrayList<>();
        List<String> sentenceList = new ArrayList<>();

        for (String sentence : sentences) {
            if (!sentence.trim().equals(""))
                sentenceList.add(sentence.trim());
        }

        length.addAll(sentenceList.stream().map(word -> word.split(" ").length).collect(Collectors.toList()));
        System.out.println(Collections.max(length));

    }

}
