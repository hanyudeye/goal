package main

//定义程序片段 main
// 有一个 a , 它的值 是5.123
// 有一个 b，它的值是 a 进行取整数
// 显示器显示文本: b 的值是
import (
	"fmt"
)

func main() {

	a := 5.123
	b := int(a)

	fmt.Println("b的值是", b)

}
