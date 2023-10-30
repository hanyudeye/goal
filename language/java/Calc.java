// 计算机通用的运算

public class Calc {
    public static void main(String[] args) {
        int a = 21, b = 31;

        // 逻辑运算，位运算，用途是测试真假，和数字运算中作为算术运算的转化
        System.out.println(a & b);
        System.out.println(a | b);
        System.out.println(a ^ b);
        System.out.println(~a);
        System.out.println(a >> 2);
        System.out.println(a << 1);

        // 数学运算
        System.out.println(a + b);
        System.out.println(a / b);
    }
}
