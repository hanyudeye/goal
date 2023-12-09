#include <getopt.h>


/* 使用C 库内置的 getopt_long 函数来快速获取选项 */

/* 假如我们内定程序要接收下面几个选项 */

/* 短选项  长选项 意图 */
/* -h         --help  显示软件的简单说明 */
/* -o filename   --output filename  指定输出的文件的名字 */
/* -v --verbose  显示软件的详细说明 */

int main(int argc, char *argv[])
{
  
  //所需要的参数
  const struct option long_options[]={
    {"help",0,NULL,'h'},
    {"output",1,NULL,'o'},
    {"verbose",0,NULL,'v'},
    {NULL,0,NULL,0}
  };


  int next_option;
  //遍历参数
  do{
    
    next_option=getopt_long(argc,argv,)

  }while(next_option != -1);

  return 0;
}
