package main

import "fmt"

var a = 1

func main() {

	switch a {
	case 1:
		fmt.Println("当前的分支是", 1)
		// 有数据类型
	case '1':
		fmt.Println("当前的分支是", '1')
	case '2':
		fmt.Println("当前的分支是", 2)
	default:
		fmt.Println("当前的分支是", "default")
	}

}
