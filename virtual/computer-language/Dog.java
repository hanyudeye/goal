public class Dog {
    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Dog() {
    }

    public Dog(String name) {
        this.name = name;
    }

    public void bark() {
        System.out.println("汪汪汪");
    }
}
