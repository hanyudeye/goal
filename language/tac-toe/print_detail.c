#include <stdio.h>

struct people
{
    /* data */
    int age;
    char *name;
};

int main(int argc, char const *argv[])
{
    // printf("output integer %d\n", 333);
    // printf("output string类型的对象 %s\n", "你好，世界！");
    struct people p1 = {33, "明哥"};
    char *welcome_Msg = "欢迎来到地球";
    int shuzu[] = {1, 5, 7};
    // printf("结构体p1的年龄是是 %d\n", p1.age);
    // printf("shuzu[1] 是 %d\n",shuzu[1]);

    // 格式化打印
    // printf("%1$.2$d\n", 99,123);
    // printf("%10d\n", 123);
    char x;
    printf("%1$.*2$d%3$hhn", 5, 10, &x);
    return 0;
}
