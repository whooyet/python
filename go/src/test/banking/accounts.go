package banking

import (
	"errors"
	"fmt"
)

type Account struct {
	owner	string
	balance int
}

var errNoMoney = errors.New("오우. 이런! 문제가 발생했어! 다시 시도하십시오.")

func NewAccount(owner string) *Account{
	account := Account{owner: owner, balance:0}
	return &account
}

// 스턱트의 첫 글자를 따서 만들어야함 그래서 a인거임
func (a *Account) Deposit(amount int) {
	fmt.Println(amount)
	a.balance += amount
}

func (a Account) Balance() int {
	return a.balance
}

func (a *Account) Withdraw(amount int) error {
	if a.balance < amount {
		return errNoMoney
	}
	a.balance -= amount
	return nil
}


func (a *Account) ChangeOwner(newOwner string) {
	a.owner = newOwner
}

//이 경우 아무 값도 변경하지 않기에 복사본을 만들 이유가 있다.
func (a Account) Owner() string {
	return a.owner
}

func (a Account) String() string {
	//return fmt.Sprint(a.Owner(), "5+5=",a.Balance(), "account.\nHas: ", a.Balance())
	return fmt.Sprint(a.Owner(), "'s account.\nHas: ", a.Balance())
}