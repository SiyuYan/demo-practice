package Polymorphism;

class Shared {
    private long counter = 0;
    private final long id = counter++;

    Shared() {
        System.out.println("id " + id);
        System.out.println("Counter " + counter);
    }


    public static void main(String[] args) {

        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
        new Shared();
    }
}