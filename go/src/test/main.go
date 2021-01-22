package main

import "fmt"

// var arr3 = [...]int{9, 8, 7, 6} //[...]을 이용한 배열 크기 자동 설정
// names := []string{"nico", "lynn", "dal"} // 같은 뜻
// wow := map[string]int{"name":57, "age":19} // string 값이 name 과 age, int 값이 57과 19

type person struct {
	name    string
	age     int
	favFood []string
}

func main() {

	favFood := []string{"kimchi", "ramen"}
	nico := person{name: "nico", age: 18, favFood: favFood}
	fmt.Println(nico.name)

	//wow := map[string]int{"name":57, "age":19}
	//for name, age := range wow {
	//	fmt.Println(name, age)
	//}

}