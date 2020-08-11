package concurrency;

import java.util.ArrayList;
import java.util.List;

public class Demo {

    private static int reverse(int x) {
        long result = 0;
        while (x != 0) {
            result = result * 10 + x % 10;
            x /= 10;
        }
        if (result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
            return 0;
        } else return (int) result;
    }

    public static void reverseString(char[] s) {
        for (int i = 0; i < s.length / 2; i++) {
            char temp;
            temp = s[i];
            s[i] = s[s.length - i - 1];
            s[s.length - i] = temp;
        }
        System.out.println(s);
    }

    static int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> myList = new ArrayList<Integer>();
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length; j++) {
                if (nums1[i] == nums2[j]) {
                    myList.add(nums1[i]);
                }
            }
        }
        return myList.stream().mapToInt(Integer::new).toArray();

    }

    public static void main(String[] args) {
//        System.out.println(intersect([1, 2, 2, 1],[2, 2]));
        int[] result;
        int array[]=new int[3];

    }
}
