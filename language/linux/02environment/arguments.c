#include <stdio.h>

/* 这个程序显示 传递给程序的参数的个数和 具体的值 */

int main(int argc, char *argv[])
{

  printf("参数的数量是%d\n",argc);

  for(argc;argc>0;argc--){
    printf("参数的当前值是%s\n",argv[argc-1]);
  }

  return 0;
}
