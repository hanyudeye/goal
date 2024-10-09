import com.fasterxml.jackson.databind.ObjectMapper;
/**
 * java
 */
public class java {

    public String name;
    public int age;
    public String gender;
    public String[] loves;

    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        int c = a + b;
        // System.out.println(c);
        // System.out.println("hello");

        java tJava = new java();
        tJava.testReadJson();


    }

    public void testReadJson() {
        String json = "{\"name\":\"张三\",\"age\":18,\"gender\":\"male\",\"loves\":[\"apple\",\"banana\",\"orange\"]}";
        System.out.println(json);

        Dog dog = new Dog("旺财");
        System.out.println(dog.getName());
        String[] data={"apple","banana","orange"};

        ObjectMapper objectMapper = new ObjectMapper();
        String s = objectMapper.writeValueAsString(data);
        System.out.println(s);

   }

}