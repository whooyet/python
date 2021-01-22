package main

import (
	"errors"
	"fmt"
	"log"
)

var errOne = errors.New("에러가 발생했습니다. 다시 시도해주세요")

func main() {
	var a, c int
	var b string

	loof := 0

	for loof < 10 {
		fmt.Println("\n뿌산기입니다. 수식으로 만들면 계산해드립니다.")
		fmt.Println("ex) 1 + 2\n")

		fmt.Scanln(&a, &b, &c)
		loof += 1

		err :=  giho(a,c,b)

		if err != nil {
			log.Fatal(err)
		}
	}
}

func giho(a, c int, b string) error {

	var d int

	switch b {
	case "+":
		d = a + c
	case "-":
		d = a - c
	case "*":
		d = a * c
	case "/":
		d = a / c
	default:
		return errOne
	}

	fmt.Println(a, "+", c, "=", d)
	return nil
}