package main

import "fmt"

func main() {
	fmt.Println(sayWorld("xiaolao第"))
	var name string
	name = "aming"
	fmt.Println(name)

	var b bool
	b = true

	fmt.Println(b)

}

func sayWorld(s string) string {
	return "Fuck" + s
}
