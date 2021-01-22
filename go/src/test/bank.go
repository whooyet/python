package main

import (
	"fmt"
	"test/banking"
)

//fmt.Print(first + " " + second)

func main() {
	account := banking.NewAccount("nico")
	account.Deposit(10)
	//err := account.Withdraw(5)
	//if err != nil {
	//	log.Fatal(err)
	//}
	fmt.Print(account)

}