#include <time.h>
#include <stdio.h>
#include <stdlib.h>

// 时间函数，显示当前时间
int main(){
    time_t timevalue;
    time(&timevalue);
    printf("当前时间是: %s",ctime(&timevalue));
    exit(0);
}