
//默认数据类型和自定义类
public class DataType {
    public static void main(String[] args) {
        int a = 123;
        String b = "abc4";
        System.out.println(b.length());
        int c[] = { 1, 3, 5 };
        System.out.println(c[1]);

        int d[][] = {
                { 11, 12, 13, 14, 15 },
                { 21, 22, 23, 24, 25 },
                { 31, 32, 33, 34, 35 }
        };
        System.out.println(d[1][1]);
        System.out.println(d.length);

    }
}

// 定制类型
class Box {
    protected double width;
}

class SmallBox extends Box {
    public void setSmallWidth(double wid) {
        width = wid;
    }

    public double getSmallWidth() {
        return width;
    }
}