package main

import "fmt"

func main() {
	var a = 5

	fmt.Println("逻辑判断", a == 5)
	fmt.Println("逻辑判断", a != 5)

	fmt.Println("逻辑判断", a|5)
	fmt.Println("逻辑判断", a&5)
}
