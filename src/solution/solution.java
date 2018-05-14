package solution;

import java.util.List;
import java.util.Objects;

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
}

