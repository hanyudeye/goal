#include <stdio.h>

/* 这个变量 environ 指向 environment 字符串数组*/
extern char** environ;

int main(int argc, char *argv[])
{
  char** var;
  for(var=environ;*var != NULL;++var){
    printf("环境变量的值是 %s\n",*var);
  }
  return 0;
}

