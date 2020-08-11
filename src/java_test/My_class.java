package java_test;

class Outer_Demo {
    private int num = 175;

    // inner class
    class Inner_Demo {
        int print() {
            System.out.println("This is an inner class");
            return num;
        }
    }

    // Accessing he inner class from the method within
    void display_Inner() {
        Inner_Demo inner = new Inner_Demo();
        inner.print();
    }
}

public class My_class {

    public static void main(String args[]) {
        // Instantiating the outer class
        Outer_Demo outer = new Outer_Demo();
        Outer_Demo.Inner_Demo inner = outer.new Inner_Demo();
        System.out.println(inner.print());
        // Accessing the display_Inner() method.
        outer.display_Inner();
    }
}
