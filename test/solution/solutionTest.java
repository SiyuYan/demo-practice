package solution;

import org.junit.Test;

import java.util.ArrayList;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.*;


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
        ArrayList<Interval> intervals = new ArrayList<Interval>();
        ArrayList<Interval> intervals2 = new ArrayList<Interval>();
        intervals.add(new Interval(5, 8));
        intervals.add(new Interval(6, 8));
        intervals2.add(new Interval(8, 9));
        intervals2.add(new Interval(3, 8));
        assertThat("Meeting", solution.meeting(intervals), is(false));
        assertThat("Meeting", solution.meeting(intervals2), is(true));
    }

    @Test
    public void testRevereString() throws Exception {

        solution solution = new solution();
        assertThat("Reverse", solution.reverse(intervals), is(false));

    }
}