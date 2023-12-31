package main

import "fmt"

var (
	常量1 = "阿西吧吧"
	常量2 = "阿东吧吧"
)

func main() {
	// 有个数字，他的值是 9527
	var i int

	fmt.Println("i=", i)

	i = 9527
	fmt.Println("i=", i)

	// 测试：我不知道常量1 表示什么了，我打印下现在的值
	fmt.Println("常量1 的值是 ", 常量1)
}
