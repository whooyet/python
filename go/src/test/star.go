package main

import "fmt"

func main() {


	count := 1
	//star := 2
	a := 1

	for count < 6 {

		if a == 1 {
			fmt.Printf("     *\n")
		}

		if a == 3 {
			fmt.Printf("    ***\n")
		}

		if a == 5 {
			fmt.Printf("   *****\n")
		}

		a += 2
		count += 1
	}
}

//     *
//    ***
//   *****
//    ***
//     * <- 이걸 구현 해보삼 불고기
