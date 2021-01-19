package main

import (
	"fmt"
)

func main() {
	var a, c, d int
	var b string

	fmt.Println("계산기임")
	fmt.Println("수식으로 만들어주세요")
	fmt.Println("ex) 1 + 2, 3 * 4 등등")

	fmt.Scanln(&a, &b, &c)

	switch b {
	case "+":
		d = a+c
		fmt.Println((d))
	case "-":
		d = a-c
		fmt.Println((a - c))
	case "*":
		d = a*c
		fmt.Println((a * c))
	case "/":
		d = a/c
		fmt.Println((a / c))
		default:
		   a = 0
		   b = "0"
		   c = 0
		   d = 0

		fmt.Println("에러가 발생했습니다. 다시 시도해주세요")
	}
	fmt.Printf("%d %s %d = %d", a, b, c, d)
}