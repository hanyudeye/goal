#include <stdio.h>

extern int add99(int source);

int main(int argc, char const *argv[])
{
    int c = 1 + 3;
    printf("nice");

    int res=add99(c);
    printf("res的结果是%d\n",res);
    return 0;
}

int add99(int source)
{
        return source + 99;
}