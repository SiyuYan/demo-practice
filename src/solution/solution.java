package solution;

import java.util.*;

class solution {

    boolean canPermutePalindrome(String s) {
        String[] array = s.split("");
        for (int num = 0; num < array.length; num++) {
            if (!Objects.equals(array[num], array[array.length - 1 - num])) {
                return false;
            }
        }
        return true;
    }

    String convertToBinary(int number) {
        String binary;
        StringBuilder value = new StringBuilder();
        while (number != 0) {
            binary = String.valueOf(number % 2);
            number = number / 2;
            value.append(binary);
        }
        return new StringBuffer(value.toString()).reverse().toString();
    }

    String convertToHex(int number) {
        String binary;
        StringBuilder value = new StringBuilder();
        while (number != 0) {
            binary = String.valueOf(number % 8);
            number = number / 8;
            value.append(binary);
        }
        return new StringBuffer(value.toString()).reverse().toString();
    }

    boolean meeting(List<Interval> intervals) {

        for (int num = 0; num < intervals.size() - 1; num++) {
            for (int index = 1; num + index <= intervals.size() - 1; index++) {
                {
                    if (intervals.get(num).end > intervals.get(num + index).start
                            && intervals.get(num).start < intervals.get(num + index).end) {
                        return false;
                    }

                }
            }
        }
        return true;
    }

    String getSubString(String str1, String str2) {
        String targetString = null;
        // 取出其中较短的字符串(照顾效率)
        String shorter = str1.length() > str2.length() ? str2 : str1;
        String longer = shorter.equals(str1) ? str2 : str1;
        // 在较短的字符串中抽取其‘所有长度’的子串，顺序由长到短
        out:
        for (int subLength = shorter.length(); subLength > 0; subLength--) {
            // 子串的起始角标由 0 开始右移，直至子串尾部与母串的尾部-重合为止
            for (int i = 0; i + subLength <= shorter.length(); i++) {
                String subString = shorter.substring(i, i + subLength); // 取子串
                if (longer.contains(subString)) { // 注意 ‘=’
                    System.out.println(subLength);
                    targetString = subString;
                    break out;
                    // 一旦满足条件，则最大子串即找到，停止循环，
                }
            }
        }
        return targetString;
    }

    /*两个字符串，判断其中一个字符串是不是另一个字符串的右移子串。如cda是abcd的右移子串。。*/


    boolean isRightSubString(String shorter, String longer) {
        char[] results = longer.toCharArray();
        char[] chars = longer.toCharArray();

        if (shorter.length() <= longer.length()) {
            do {
                char temp = chars[longer.length() - 1];
                System.arraycopy(chars, 0, chars, 1, longer.length() - 1);
                chars[0] = temp;
                String srcStr = String.valueOf(chars);
                if (srcStr.contains(shorter))
                    return true;
            } while (!Arrays.equals(chars, results));
        }
        return false;
    }

    /* 给出一个字符串，求最长对称子字符串的长度，如输入google，则输出为4。*/

    int MaxPalindromicString(String s) {
        if (s.length() == 1) {
            return 1;
        }
        for (int i = 0; i < s.length(); i++) {


        }


        return 0;
    }

    public static void main(String[] args) {
        int[] case1 = new int[]{5,1,2,3,4};
        System.out.println(args);
        String[] text = new String[]{"the weather is good ", "today is good", "today has good weather", "good weather is good"};
        HashMap<String, Integer> hashMap = new HashMap<>();
        for (String temp : text) {
            String[] words = temp.split("\\s");
            for (String word : words) {
                if (!hashMap.containsKey(word)) {
                    hashMap.put(word, 1);
                } else {
                    int k = hashMap.get(word) + 1;
                    hashMap.put(word, k);
                }
            }
        }
        for (Object word : hashMap.keySet()) {
            System.out.println(word + ":" + hashMap.get(word));
        }
    }

}

