using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HelloWorld//命名空间
{
    class hello//类
    {
        static void Main(string[] args)//main函数
        {
string str = "Hello World !";//声明一个叫“str”的string类型的变量，并将它的值初始化为“Hello World !”
Console.WriteLine(str);//Console指“控制台类”，WriteLine是控制台类里的用于输出字符串的“方法”
Console.ReadKey();//其实前两行已经达到我们的目的了，这行是要程序等我们输入一个字符后再结束程序
        }
    }
}