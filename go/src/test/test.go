package main

import (
	"fmt"
	"strings"
)

var c = 4

func aa(name string) (int, string) {
	return len(name), strings.ToUpper(name)
}

func bb(name string) (wow int, up string) {
	defer fmt.Println("end")
	wow = len(name)
	up = strings.ToUpper(name)
	return
}

func superAdd(num ...int) int {
	total := 0
	for number := range num {
		total += number
	}
	return total
}

func check(age int) bool {
	if KoreanAge := age + 2; KoreanAge < 20 {
		return false
	}

	//KoreanAge := age + 2
	//if(KoreanAge < 20) {
	//	return false
	//}

	return true
}


func main() {
	fmt.Println(superAdd(1, 2, 3, 4, 5, 6))
	//fmt.Println(bb("Hello"))
	//repeatMe("a", "b", "c", "d")
	//thing.SayHello()
	//fmt.Println(aot("ddddd"))
}
