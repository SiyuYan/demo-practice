package solution;

import org.junit.Test;

import java.util.ArrayList;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class solutionTest {
    @Test
    public void testPermutePalindrome() throws Exception {

        solution solution = new solution();
        assertThat("one", solution.canPermutePalindrome("aab"), is(false));
        assertThat("two", solution.canPermutePalindrome("abba"), is(true));

    }

    @Test
    public void testMeeting() throws Exception {
        solution solution = new solution();
        ArrayList<Interval> intervals = new ArrayList<>();
        ArrayList<Interval> intervals2;
        intervals2 = new ArrayList<>();
        intervals.add(new Interval(5, 8));
        intervals.add(new Interval(6, 8));
        intervals2.add(new Interval(8, 9));
        intervals2.add(new Interval(3, 8));
        assertThat("Meeting", solution.meeting(intervals), is(false));
        assertThat("Meeting", solution.meeting(intervals2), is(true));
    }

    //    @Test
//    public void testRevereString() throws Exception {
//
//        solution solution = new solution();
//        assertThat("Reverse", solution.reverse("ab "), is("ba"));
//        assertThat("Reverse", solution.reverse("  hello this"), is("olleh siht"));
//        assertThat("Reverse", solution.reverse("Siyu  Practice  "), is("uyiS ecitcarP"));
//
//    }
    @Test
    public void testConvertToBinary() throws Exception {
        solution solution = new solution();
        assertThat("ConvertToBinary", solution.convertToBinary(5), is("101"));
        assertThat("ConvertToBinary", solution.convertToBinary(6), is("110"));
    }

    @Test
    public void convertToHex() throws Exception {
        solution solution = new solution();
        assertThat("convertToHex", solution.convertToHex(796), is("1434"));
    }

    @Test
    public void subString() throws Exception {
        solution solution = new solution();
        String str1 = "asdfdfdfdfdfdfdfdfdfasf34lk343434343433333fdasfd";
        String str2 = "asdfdfdfdfdfdfdfdfdf3434343434343jfshasdazlzlasbfasfdllzlz";

        assertThat("MaxSubString", solution.getSubString(str1, str2), is("asdfdfdfdfdfdfdfdfdf"));
    }

    @Test
    public void testRightSubString() throws Exception {
        solution solution = new solution();

        assertThat("cda", solution.isRightSubString("cda", "abcd"), is(true));
        assertThat("cda", solution.isRightSubString("acd", "abcd"), is(false));
        assertThat("abc", solution.isRightSubString("abc", "abcd"), is(true));
        assertThat("bcd", solution.isRightSubString("bcd", "abcd"), is(true));
        assertThat("", solution.isRightSubString("", "abcd"), is(true));
        assertThat("xxxx", solution.isRightSubString("xxxx", "abcd"), is(false));
        assertThat("abcde", solution.isRightSubString("abcde", "abcd"), is(false));
    }


}